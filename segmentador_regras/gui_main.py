import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QTextEdit, QPushButton, QCheckBox, QLabel, QFileDialog, 
    QFrame, QScrollArea, QMessageBox, QPlainTextEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon

from utils import utils
from segmentador.segmentador import segmentador_de_edus

class EduSegmenterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Segmentador de EDUs")
        self.setMinimumSize(800, 700)
        
        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Title
        title_label = QLabel("Segmentador de Unidades Discursivas Elementares (EDUs)")
        title_label.setObjectName("titleLabel")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # Input Section
        input_label = QLabel("Texto de Entrada:")
        input_label.setObjectName("sectionLabel")
        main_layout.addWidget(input_label)

        self.input_text = QPlainTextEdit()
        self.input_text.setPlaceholderText("Cole o texto aqui ou carregue um arquivo...")
        main_layout.addWidget(self.input_text)

        button_layout = QHBoxLayout()
        self.load_btn = QPushButton("📂 Carregar Arquivo .txt")
        self.load_btn.clicked.connect(self.load_file)
        button_layout.addWidget(self.load_btn)
        button_layout.addStretch()
        main_layout.addLayout(button_layout)

        # Rules Section
        rules_group = QFrame()
        rules_group.setObjectName("rulesGroup")
        rules_layout = QVBoxLayout(rules_group)
        
        rules_title = QLabel("Regras de Segmentação:")
        rules_title.setObjectName("rulesTitle")
        rules_layout.addWidget(rules_title)

        # Rule 1 (Mandatory)
        self.check_r1 = QCheckBox("Regra 1: Ponto Final (Obrigatória)")
        self.check_r1.setChecked(True)
        self.check_r1.setEnabled(False)
        rules_layout.addWidget(self.check_r1)

        # Optional Rules
        self.check_r9_3 = QCheckBox("Regras 9 & 3: Informações Parentéticas e Citações")
        self.check_r2 = QCheckBox("Regra 2: Marcadores Fortes")
        self.check_r5 = QCheckBox("Regra 5: Verbo Implícito")
        self.check_r6 = QCheckBox("Regra 6: Orações Reduzidas")
        self.check_r7 = QCheckBox("Regra 7: Orações Relativas")
        self.check_r8 = QCheckBox("Regra 8: Verbos Públicos/Atribuição")

        # Set defaults based on main.py behavior (all on?)
        for cb in [self.check_r9_3, self.check_r2, self.check_r5, self.check_r6, self.check_r7, self.check_r8]:
            cb.setChecked(True)
            rules_layout.addWidget(cb)

        main_layout.addWidget(rules_group)

        # Action Section
        self.segment_btn = QPushButton("🚀 Segmentar Texto")
        self.segment_btn.setObjectName("segmentBtn")
        self.segment_btn.setFixedHeight(50)
        self.segment_btn.clicked.connect(self.run_segmentation)
        main_layout.addWidget(self.segment_btn)

        # Output Section
        output_label = QLabel("Resultado da Segmentação:")
        output_label.setObjectName("sectionLabel")
        main_layout.addWidget(output_label)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        main_layout.addWidget(self.output_text)

        save_layout = QHBoxLayout()
        self.save_btn = QPushButton("💾 Salvar em .txt")
        self.save_btn.clicked.connect(self.save_file)
        self.save_btn.setEnabled(False)
        save_layout.addStretch()
        save_layout.addWidget(self.save_btn)
        main_layout.addLayout(save_layout)

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f7f9;
            }
            #titleLabel {
                font-size: 22px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 10px;
            }
            #sectionLabel {
                font-size: 16px;
                font-weight: bold;
                color: #34495e;
            }
            QPlainTextEdit, QTextEdit {
                background-color: #ffffff;
                border: 1px solid #dcdde1;
                border-radius: 8px;
                padding: 10px;
                font-family: 'Segoe UI', Arial;
                font-size: 14px;
            }
            #rulesGroup {
                background-color: #ffffff;
                border: 1px solid #dcdde1;
                border-radius: 8px;
                padding: 15px;
            }
            #rulesTitle {
                font-weight: bold;
                font-size: 14px;
                margin-bottom: 5px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            #segmentBtn {
                background-color: #2ecc71;
                font-size: 16px;
            }
            #segmentBtn:hover {
                background-color: #27ae60;
            }
            QCheckBox {
                font-size: 13px;
                spacing: 10px;
            }
        """)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            try:
                content = utils.return_text_from_file(file_path)
                self.input_text.setPlainText(content)
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Não foi possível ler o arquivo:\n{str(e)}")

    def run_segmentation(self):
        text = self.input_text.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "Aviso", "Por favor, insira um texto para segmentar.")
            return

        self.segment_btn.setEnabled(False)
        self.segment_btn.setText("Processando...")
        QApplication.processEvents()

        try:
            # Step 1: Tokenize
            tokens = utils.tokenizer_spacy(text)
            
            # Step 2: Remove singles
            tokens = utils.remove_tokens_singles(tokens)
            
            # Step 3: Rule 1 (Mandatory)
            data = segmentador_de_edus.regra_1(tokens)
            
            # Step 4: Optional Rules in order
            if self.check_r9_3.isChecked():
                data = segmentador_de_edus.regra_9_3(data)
            
            if self.check_r2.isChecked():
                data = segmentador_de_edus.regra_2(data, utils.marcadores_fortes_lista())
            
            if self.check_r7.isChecked():
                data = segmentador_de_edus.regra_7(data)
            
            if self.check_r5.isChecked():
                data = segmentador_de_edus.regra_5(data)
            
            if self.check_r6.isChecked():
                data = segmentador_de_edus.regra_6(data)
            
            if self.check_r8.isChecked():
                data = segmentador_de_edus.regra_8(data)
            
            # Step 5: Convert back to text
            final_edus = utils.retorna_texto(data)
            
            # Display result
            result_text = "\n".join([f"[{i+1}] {edu.strip()}" for i, edu in enumerate(final_edus)])
            self.output_text.setPlainText(result_text)
            self.save_btn.setEnabled(True)

        except Exception as e:
            QMessageBox.critical(self, "Erro no Processamento", f"Ocorreu um erro ao segmentar o texto:\n{str(e)}")
        finally:
            self.segment_btn.setEnabled(True)
            self.segment_btn.setText("🚀 Segmentar Texto")

    def save_file(self):
        result = self.output_text.toPlainText()
        if not result:
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Resultado", "segmentacao.txt", "Text Files (*.txt)")
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(result)
                QMessageBox.information(self, "Sucesso", "Arquivo salvo com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Não foi possível salvar o arquivo:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EduSegmenterApp()
    window.show()
    sys.exit(app.exec())
