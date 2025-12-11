from flask import Blueprint, render_template, request, redirect, url_for
from models import Review

# Blueprintの作成
review_bp = Blueprint('review', __name__, url_prefix='/reviews')


@review_bp.route('/')
def list():
    
    # データ取得
    reviews = Review.select()

    return render_template('review_list.html', title='レビュー一覧', items=reviews)


@review_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        rating = request.form['rating']
        comment = request.form['comment']
        Review.create(rating=rating, comment=comment)
        return redirect(url_for('review.list'))
    
    return render_template('review_add.html')


@review_bp.route('/edit/<int:review_id>', methods=['GET', 'POST'])
def edit(review_id):
    review = Review.get_or_none(Review.id == review_id)
    if not review:
        return redirect(url_for('review.list'))

    if request.method == 'POST':
        review.rating = request.form['rating']
        review.comment = request.form['comment']
        review.save()
        return redirect(url_for('review.list'))

    return render_template('review_edit.html', review=review)