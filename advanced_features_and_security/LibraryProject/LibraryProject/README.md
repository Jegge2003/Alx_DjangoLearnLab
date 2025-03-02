# Security Enhancements for Django Application

## Configured HTTPS and Secure Headers

1. Enforced HTTPS with `SECURE_SSL_REDIRECT = True`
2. Configured HSTS to prevent downgrade attacks:
   - `SECURE_HSTS_SECONDS = 31536000`
   - `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
   - `SECURE_HSTS_PRELOAD = True`
3. Secured cookies:
   - `SESSION_COOKIE_SECURE = True`
   - `CSRF_COOKIE_SECURE = True`
4. Implemented secure headers:
   - `X_FRAME_OPTIONS = "DENY"`
   - `SECURE_CONTENT_TYPE_NOSNIFF = True`
   - `SECURE_BROWSER_XSS_FILTER = True`

## Deployment Instructions
1. Obtain an SSL certificate (e.g., Let's Encrypt).
2. Configure the web server (Nginx, Apache) to serve HTTPS.
3. Restart the Django application to apply changes.

These changes improve security by preventing session hijacking, XSS, and clickjacking attacks.
