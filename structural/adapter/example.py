class RenderTemplate:
    def render_header(self, ): pass
    def render_body(self, ): pass
    def render_footer(self, ):pass


class RenderHTML(RenderTemplate):
    def render_header(self):
        return super().render_header()
    
    def render_body(self):
        return super().render_body()
    
    def render_footer(self):
        return super().render_footer()


class PDFTemplate:
    def render_top(self, ): pass
    def render_middle(self, ): pass
    def render_bottom(self, ): pass

class RenderPDF(PDFTemplate):
    def render_top(self):
        return super().render_top()
    
    def render_middle(self):
        return super().render_middle()
    
    def render_bottom(self):
        return super().render_bottom()


class PDFAdaper(RenderTemplate):
    template = None
    def __init__(self, template: PDFTemplate)  :
        self.template = template

    def render_header(self):
        return self.template.render_top()
    
    def render_body(self):
        return self.template.render_middle()
    
    def render_footer(self):
        return self.template.render_bottom()


pdf_template = PDFTemplate()
pdf_template_adapter = PDFAdaper(pdf_template)
pdf_template_adapter.render_footer()