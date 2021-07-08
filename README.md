# Lambda function to parse Redshift Event Subscription Notifications from SNS

This Lambda has 2 sections. 1. Variables and 2. Main body

<b><h3> Variables </h3> </b>

1. parsed_sns_arn = '' - Enter the ARN of the SNS topic you created that the Lambda function should publish to for event ID's that are parsed as "true"
2. check_list = [ ] - This is a list of Redhsift Notification Subscription event ID's you want to evaluate for. E.G. ['3000', '3520, '3519']

<b><h3> Main Body </h3></b>
Line 12 creates the SNS client

Line 14 defines the Lambda handler

Lines 17-18 pulls the SNS json and parses down to the "About this Event" key in Records>Sns>Message

Lines 20-26 loop through the check_list variable and search the SNS topic message for each of the event Id's in the list.

Lines 29-32 Publishes a custom message and subject to the parse_sns_arn variable when an event ID from check_list variable is found
