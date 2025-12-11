from datetime import datetime, date
from peewee import fn
from .order import Order
from .product import Product


class Report:
    @staticmethod
    def get_total_sales():
        """全期間の総売上を取得"""
        try:
            query = (Order
                    .select(fn.SUM(Product.price).alias('total'))
                    .join(Product)
                    .scalar())
            return float(query) if query else 0
        except:
            return 0
    
    @staticmethod
    def get_monthly_sales(year=None, month=None):
        """指定された月の売上を取得（デフォルトは当月）"""
        if year is None or month is None:
            today = date.today()
            year = today.year
            month = today.month
        
        start_date = datetime(year, month, 1)
        if month == 12:
            end_date = datetime(year + 1, 1, 1)
        else:
            end_date = datetime(year, month + 1, 1)
        
        try:
            query = (Order
                    .select(fn.SUM(Product.price).alias('monthly_total'))
                    .join(Product)
                    .where(Order.order_date.between(start_date, end_date))
                    .scalar())
            return float(query) if query else 0
        except:
            return 0
    
    @staticmethod
    def get_monthly_sales_data():
        """月別売上データを取得（過去12ヶ月分）"""
        monthly_data = []
        today = date.today()
        
        for i in range(12):
            if today.month - i > 0:
                year = today.year
                month = today.month - i
            else:
                year = today.year - 1
                month = 12 + (today.month - i)
            
            sales = Report.get_monthly_sales(year, month)
            monthly_data.append({
                'year': year,
                'month': month,
                'sales': sales
            })
        
        return monthly_data[::-1]  # 古い順に並び替え