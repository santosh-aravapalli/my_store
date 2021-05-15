class Routers:
    """
    A router to control all database operations on models in the
    user application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to users_db.
        """
        cms_consents_tables = ['CONSENTS_REQUESTS']
        if model._meta.db_table in cms_consents_tables:
            return 'consents_db'

        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to users_db.
        """
        cms_consents_tables = ['CONSENTS_REQUESTS']
        if model._meta.db_table in cms_consents_tables:
            return 'consents_db'
            
        return None



