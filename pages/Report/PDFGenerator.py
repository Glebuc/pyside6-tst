from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import re

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.document = SimpleDocTemplate(self.filename, pagesize=A4)
        self.elements = []
        self.styles = getSampleStyleSheet()
        pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
        self.styles.add(ParagraphStyle(name='TitleStyle', fontName='DejaVuSans', fontSize=24, leading=28, spaceAfter=20))
        self.styles.add(ParagraphStyle(name='SubTitleStyle', fontName='DejaVuSans', fontSize=12, leading=22, spaceAfter=15))
        self.styles.add(ParagraphStyle(name='ContentStyle', fontName='DejaVuSans', fontSize=14, leading=12, spaceAfter=5))
        self.styles.add(ParagraphStyle(name='TestOutput', fontName='DejaVuSans', fontSize=7, leading=5, spaceAfter=5))
        self.test_titles = []  # Список для хранения названий тестов

    def create_title_page(self, title, subtitle):
        self.elements.append(Paragraph(title, self.styles['TitleStyle']))
        self.elements.append(Paragraph(subtitle, self.styles['SubTitleStyle']))
        self.elements.append(Spacer(1, 0.5 * inch))
        self.elements.append(PageBreak())

    def create_toc(self):
        self.elements.append(Paragraph("Содержание отчета", self.styles['TitleStyle']))
        toc_data = []
        for i, title in enumerate(self.test_titles):
            toc_data.append([Paragraph(f'<a href="#{i}">{title}</a>', self.styles['ContentStyle'])])
        table = Table(toc_data, colWidths=[7 * inch])
        table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TEXTCOLOR', (0, 0), (-1, -1), (0, 0, 0))
        ]))
        self.elements.append(table)
        self.elements.append(PageBreak())

    def create_test_result_page(self, test, index):
        self.elements.append(Spacer(1, 1 * inch))
        test_name = test.get('test_name', 'Unknown Test')
        self.elements.append(Paragraph(f'<a name="{index}"/>Название теста: {test_name}', self.styles['ContentStyle']))
        self.elements.append(Paragraph("Конфигурация запуска теста:", self.styles['ContentStyle']))
        for key, value in test['config'].items():
            self.elements.append(Paragraph(f"{key}: {value}", self.styles['ContentStyle']))
        self.elements.append(Paragraph("Вывод результата теста:", self.styles['ContentStyle']))
        result_test = test['result_test'].replace('\\n', '\n')
        paragraphs = result_test.split('\n')
        for paragraph in paragraphs:
            self.elements.append(Paragraph(paragraph, self.styles['TestOutput']))
        self.elements.append(PageBreak())

    def generate(self, title, subtitle, test_results):
        self.create_title_page(title, subtitle)
        self.test_titles = [test['test_name'] for test in test_results]  # Собрать названия тестов
        self.create_toc()  # Создать содержание
        for index, test in enumerate(test_results):
            self.create_test_result_page(test, index)
        self.document.build(self.elements)