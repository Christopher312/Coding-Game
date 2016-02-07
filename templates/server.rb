require 'rest-client'
require 'json'

CLIENT_ID = ENV['e101d89e649e0beae1eb']
CLIENT_SECRET = ENV['2a2bf53ce7286342434fa49aed3e07d79f6aadd3']

get '/' do
  erb :index, :locals => {:client_id => e101d89e649e0beae1eb}
end
