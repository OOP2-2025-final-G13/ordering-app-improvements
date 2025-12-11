from flask import Blueprint, render_template, request
from models.report import Report

report = Blueprint('report', __name__, url_prefix='/report')

@report.route('/')
def list():
    # 総売上を取得
    total_sales = Report.get_total_sales()
    
    # 当月売上を取得
    current_month_sales = Report.get_monthly_sales()
    
    # 月別売上データを取得
    monthly_data = Report.get_monthly_sales_data()
    
    # 特定の年月での検索があった場合
    year = request.args.get('year', type=int)
    month = request.args.get('month', type=int)
    selected_month_sales = None
    
    if year and month:
        selected_month_sales = Report.get_monthly_sales(year, month)
    
    return render_template('report_list.html', 
                         title='統計', 
                         total_sales=total_sales,
                         current_month_sales=current_month_sales,
                         monthly_data=monthly_data,
                         selected_month_sales=selected_month_sales,
                         selected_year=year,
                         selected_month=month)