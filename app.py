from flask import Flask, render_template

app = Flask(__name__)

# Sample data for blog posts (you can replace this with a database)
blog_posts = [
    {
        'title': 'First Post',
        'content': 'This is the content of the first blog post.'
    },
    {
        'title': 'Second Post',
        'content': 'This is the content of the second blog post.'
    }
]

# Define a route for the home page
@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

# Define a route for viewing individual blog posts
@app.route('/post/<int:post_id>')
def post(post_id):
    if 0 <= post_id < len(blog_posts):
        return render_template('post.html', post=blog_posts[post_id])
    else:
        return "Post not found."

# Define a route for the blog page
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Define a route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Define a route for the photography page
@app.route('/photography')
def photography():
    return render_template('photography.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

