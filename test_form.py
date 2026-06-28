import urllib.request
import urllib.parse
import http.cookiejar
import re

# Django server URL
base_url = "http://127.0.0.1:8000"

# Setup cookie jar and opener
cookie_jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
urllib.request.install_opener(opener)

# Get CSRF token first
print("Getting CSRF token...")
response = urllib.request.urlopen(f"{base_url}/about")
html = response.read().decode('utf-8')

# Parse the response to get CSRF token
csrf_match = re.search(r'<input[^>]+name=[\'"]csrfmiddlewaretoken[\'"][^>]*value=[\'"]([^\'"]+)[\'"]', html)
if csrf_match:
    csrf_token = csrf_match.group(1)
    print(f"✓ CSRF token found: {csrf_token[:20]}...")
else:
    print("✗ CSRF token not found!")
    csrf_token = ""

# Test form data
test_data = {
    'txt1': '42',
    'txt2': '58',
    'csrfmiddlewaretoken': csrf_token
}

# Submit the form
print("\n" + "="*50)
print("Submitting form with test data:")
print(f"  - Number 1 (txt1): {test_data['txt1']}")
print(f"  - Number 2 (txt2): {test_data['txt2']}")
print("="*50 + "\n")

encoded_data = urllib.parse.urlencode(test_data).encode('utf-8')
try:
    response = urllib.request.urlopen(f"{base_url}/process", encoded_data)
    html = response.read().decode('utf-8')
    
    # Extract the sum from the response
    sum_match = re.search(r'sum is (\d+)', html)
    if sum_match:
        result_sum = sum_match.group(1)
        print(f"\n✓ Response received!")
        print(f"  - Result Sum: {result_sum}")
        print(f"  - Expected Sum: {int(test_data['txt1']) + int(test_data['txt2'])}")
        print("\n✅ Form test completed successfully!")
    else:
        print("Response:", html[:500])
        
except Exception as e:
    print(f"Error: {e}")
