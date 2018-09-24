from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.targetingsearch import TargetingSearch
from facebook_business.adobjects.targeting import Targeting
import datetime
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adimage import AdImage

access_token = ''
app_secret = ''
app_id = ''
ad_account_id = 'act_'
page_id = ''
FacebookAdsApi.init(access_token=access_token)


params = {
	'name': 'ENTER CAMPAIGN NAME HERE',
	'objective': 'POST_ENGAGEMENT',
	'status': 'ACTIVE',
}

campaign_result = AdAccount(ad_account_id).create_campaign(params=params)
print(campaign_result)

today = datetime.date.today()
start_time = str(today)
end_time = str(today + datetime.timedelta(weeks=1))

adset = AdSet(parent_id=ad_account_id)
adset.update({
    'name': 'ENTER ADSET NAME HERE',
    'campaign_id': campaign_result["id"],
    'daily_budget': 150,
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'REACH',
    'bid_amount': 10,
    'targeting': {'geo_locations': {'countries': {'TR'}},
				  'publisher_platforms': 'facebook'},
    'start_time': start_time,
    'end_time': end_time,
})

adset.remote_create(params={'status': 'ACTIVE'})

print(adset)

image = AdImage(parent_id=ad_account_id)
image[AdImage.Field.filename] = 'ENTER AD IMAGE PATH HERE'
image.remote_create()

image_hash = image[AdImage.Field.hash]
print(image)

fields = [
]
params = {
  'name': 'ENTER CREATIVE NAME HERE',
  'object_story_spec': {'page_id':page_id,'link_data':{'image_hash':image_hash,'link':'ENTER FACEBOOK PAGE LINK-PAGE_ID HERE','message':'ENTER AD MESSAGE HERE'}},
}
adcreative = AdAccount(ad_account_id).create_ad_creative(fields=fields, params=params)
print(adcreative)

fields = [
]
params = {
  'name': 'ENTER AD NAME HERE',
  'adset_id': adset['id'],
  'creative': {'creative_id': adcreative['creative_id']},
  'status': 'ACTIVE'
}
print(AdAccount(ad_account_id).create_ad(fields=fields, params=params))

