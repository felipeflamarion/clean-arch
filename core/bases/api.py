class APIBase:
    def __init__(self, *args, **kwargs):
        pass

    def _create_methods_functions(self):
        for method, view_func in self.set_methods().items():
            self.app.add_url_rule(
                rule=self.rule,
                endpoint=f"{self.endpoint}.{method.lower()}",
                view_func=view_func,
                methods=[method],
            )

    def register_api(self, app, rule, endpoint):
        self.app = app
        self.rule = rule
        self.endpoint = endpoint
        self._create_methods_functions()

    def set_methods(self):
        return {}
