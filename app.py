from app import create_app

# 16.171.13.234:5000

app = create_app()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# rsync -av --exclude='.git/' \
#     --exclude='.DS_Store' \
#     --exclude='__pycache__' \
#     --exclude='.gitignore' \
#     --exclude='.env' \
#     -e "ssh -i /Users/macbookpro/Downloads/wssfb.pem" \
#     ./ \
#     ec2-16-171-13-234.eu-north-1.compute.amazonaws.com:/home/ec2-user/AutomationFlask/

# gunicorn -w 3 app:app