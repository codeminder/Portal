menu = [{'title': "0 сайте", 'url_name': 'about'}, 
        {'title': "Добавить статью", 'url_name': 'add_page'}, 
        {'title': "Обратная связь", 'url_name': 'contact'}, 
        {'title': "Войти", 'url_name': 'Login'}
]

class DataMixin:
    
    def get_user_context(self, **kwargs): 
        
        context = kwargs 
        context['menu'] = menu
        
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        
        return context