from apify_client import ApifyClient

# Initialize the ApifyClient with your Apify API token
# Replace '<YOUR_API_TOKEN>' with your token.
client = ApifyClient("17568ce135812d9077a7a979ed78c5e3")

# Prepare the Actor input
run_input = {
    "proxyType": "http",
    "proxyAddress": "8.8.8.8",
    "proxyPort": 8080,
    "userAgent": "Chrome 131.0.6778.205",
}

# Run the Actor and wait for it to finish
run = client.actor("petr_cermak/anti-captcha-recaptcha").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)