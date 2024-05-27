from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
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
        self.styles.add(
            ParagraphStyle(name='ContentStyle', fontName='DejaVuSans', fontSize=10, leading=12, spaceAfter=5))

    def create_title_page(self, title, subtitle):
        self.elements.append(Paragraph(title, self.styles['TitleStyle']))
        self.elements.append(Paragraph(subtitle, self.styles['SubTitleStyle']))
        self.elements.append(Spacer(1, 0.5 * inch))  # Уменьшаем промежуток до 0.5 дюйма
        self.elements.append(PageBreak())  # Add a page break

    def create_test_result_page(self, test):
        self.elements.append(Spacer(1, 1 * inch))  # Add some space at the start of each test page
        test_name = test.get('test_name',
                             'Unknown Test')  # Получить значение 'test_name' или установить значение по умолчанию
        self.elements.append(Paragraph(f"Название теста: {test_name}", self.styles['ContentStyle']))
        result_test = test['result_test'].replace('\\n', '\n')  # Replace '\n' with actual newline
        paragraphs = result_test.split('\n')  # Split text into paragraphs
        for paragraph in paragraphs:
            self.elements.append(
                Paragraph(paragraph, self.styles['ContentStyle']))  # Add each paragraph as a separate element
        self.elements.append(Paragraph("Конфигурация запуска теста:", self.styles['ContentStyle']))
        for key, value in test['config'].items():
            self.elements.append(Paragraph(f"{key}: {value}", self.styles['ContentStyle']))
        self.elements.append(PageBreak())  # Add a page break after each test

    def generate(self, title, subtitle, test_results):
        self.create_title_page(title, subtitle)
        for test in test_results:  # Итерация по списку test_results
            self.create_test_result_page(test)
        self.document.build(self.elements)


