require 'net/https'
require 'json'

uri = URI('https://api.clever.com/v1.1/sections?limit=382')

http = Net::HTTP.new(uri.host, uri.port)
http.use_ssl = true
http.verify_mode = OpenSSL::SSL::VERIFY_PEER

request = Net::HTTP::Get.new(uri.request_uri)
request.add_field 'Authorization', 'Bearer DEMO_TOKEN'

response = http.request(request)

total_students = 0
JSON.parse(response.body)["data"].each do |section|
  total_students += section["data"]["students"].count
end

number_of_sections = 382
puts total_students/number_of_sections
