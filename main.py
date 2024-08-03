from website import create_app
from website  import db  

from website.models import Customer,Order,Cart,Product


app = create_app()

@app.shell_context_processor
def make_shell_context():
    return dict(
        Customer=Customer,
        Order=Order,
        Cart=Cart,
        Product=Product,
        db=db  # Include database in shell context for easy access to models.
    )

if __name__ == '__main__':
     app.run(debug=True)
     