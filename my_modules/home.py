

class HomeDisplay:
    APP_DESCRIPTION = [
		{
			"type": "image",
			# "image_url": "https://ibb.co/WFrWHK8",
			"image_url": "https://i.ibb.co/jGCv840/Banner.png",
			"alt_text": "marg"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":zap: *Hello, productivity superheroes!*"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "It's time to meet your sidekick, Peachy, powered by the latest *Google PaLM 2* model. With its lightning-fast responses, clever suggestions, and witty banter, together we'll conquer deadlines, tackle challenges, and conquer the world (of work)!\n With Peachy, you can: \n 1. Customize Tonality of the bot's responses\n 2. Have context-aware conversations\n 3. Complete complex tasks."
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":speech_balloon: *Try the following prompts:*"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "• Generate code comments for my Korean colleague \n • Design a collaborative filtering algorithm for personalized movie recommendations. \n • Draft a Holiday marketing plan for an ecommerce platform"
			}
		}
	]
    def __init__(self, client, event, logger):
        self.client = client
        self.event = event
        self.logger = logger

    def display_home(self):
        try:
            self.client.views_publish(
                user_id=self.event["user"],
                view={
                "type": "home",
                "callback_id": "home_view",
                "blocks": 
                    self.APP_DESCRIPTION  # Reference the APP_DESCRIPTION variable here
                
            }
            )
        except Exception as e:
            self.logger.error(f"Error in display_home: {str(e)}")