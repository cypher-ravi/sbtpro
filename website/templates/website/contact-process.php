<?php

	// FIRST: 
	// Instead of test@test.com put the email address of the mailing list

	$emailTo = 'test@test.com'; // Change with your Email address
	$contactSubject = 'Contact Form Website'; // Change Subject

	// SECOND:
	// save this file, and close it. Thank you!


	$contactName = $contactEmail = $contactMessage = "";

	$contactName = test_input($_POST["contactName"]);
	
	if(trim($_POST['contactEmail']) === '')  {
		$emailError = 'Forgot to enter in your e-mail address.';
		$hasError = true;
	} else if (!preg_match("/^[[:alnum:]][a-z0-9_.-]*@[a-z0-9.-]+\.[a-z]{2,4}$/i", trim($_POST['contactEmail']))) {
		$emailError = 'You entered an invalid email address.';
		$hasError = true;
	} else {
		$contactEmail = test_input($_POST['contactEmail']);
	}

	$contactSubject = test_input($_POST["contactSubject"]);

	$contactMessage = isset( $_POST["contactMessage"] ) ? preg_replace( "/(From:|To:|BCC:|CC:|Subject:|Content-Type:)/", "", test_input($_POST['contactMessage']) ) : "";

	function test_input($data) {
		$data = trim($data);
		$data = stripslashes($data);
		$data = htmlspecialchars($data);
		return $data;
	}


	if(!isset($hasError)) {
		mail($emailTo, $contactSubject, $contactMessage, "From: " . $contactName . " <" . $contactEmail . ">");
	}
	
?>