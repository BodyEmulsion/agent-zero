
from python.helpers import api, profiles

@api.route('/api/profiles', methods=['GET'])
async def list_profiles(request):
    return api.response(profiles.list_profiles())

@api.route('/api/profiles/set', methods=['POST'])
async def set_profile(request):
    data = await request.json()
    profile_name = data.get('profile')
    if not profile_name:
        return api.error('Profile name is required')
    return api.response(profiles.set_profile(profile_name))

@api.route('/api/profiles/create', methods=['POST'])
async def create_profile(request):
    data = await request.json()
    profile_name = data.get('name')
    if not profile_name:
        return api.error('Profile name is required')
    return api.response(profiles.create_profile(profile_name))
