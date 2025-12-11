from .user import user_bp
from .product import product_bp
from .order import order_bp
from .report import report
from .review import review_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  product_bp,
  order_bp,
  report,
  review_bp
]
