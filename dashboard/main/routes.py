from dashboard.main import bp

@bp.route('/')
@bp.route('/dashboard/<int:test>')
def dashboard(test=2):
    return '<h2>{test} will appear</h2>'
