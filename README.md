# WhatsAppURL
## Description
This is a simple tool to generate WhatsApp URLs and message the recipient without adding them into your address book first.
The generated URLs would automatically launch/open the installed WhatsApp application on your mobile devices or computers.
This tool also helps to format the recipients number to conform to WhatsApp API requirements.

## Background
This tool was created due to the following encounters:
1. The need to quickly message someone without saving their number in your phone/computer's address book and waiting for WhatsApp to sync the new contact.
2. Manually formatting contact numbers and forming the WhatsApp URL to message them.
3. Companies may have a WhatsApp shortcut that is malformed / using wrong API which is no longer usable.

# Changelog
## v1.0 - 23 Oct 2023
- Rename button and instructions.
- Added new button to generate URL and auto open WhatsApp.
- Change field 'Country' default from Afghanistan to a 'tooltip' unless auto detected.
- Select2 to initialize first while country detection is in progress/not detected.
- Ensure form is filled in before submission to generate the URL.
- Removed old files.
- Made both GitHub and version buttons go to GitHub repository in new window

## v0.3 - 11 Oct 2023
- Used Start Bootstrap's Scrolling Nav page.
- Removed auto opening of URL to allow users to verify the URL and then select it.

## v0.2 - 28/29 Sep 2023
- Added Select2 for easier selection of country name / country calling code.
- Added geolocation detection to default selection of country name / country calling code based on IP address.
- Improved instructions.
- Added Ko-Fi link
- Added versioning and GitHub profile link.

## v0.1 - 05/06 Apr 2023
- Initial version based on ISO 3166 Alpha 3 codes.
- Generate WhatsApp URL based on user's selection and input.

# Backlog
- Paste number and allow detection of country code if it is part of it?
- Add license and T&Cs