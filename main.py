from app import create_app

# This is required for Vercel serverless deployment
app = create_app()
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001)
