<?php
// Get the form data
$name = $_POST['name'];
$email = $_POST['email'];
$bloodType = $_POST['bloodType'];
$phone = $_POST['phone'];
$dob = $_POST['dob'];
$lastDonation = $_POST['lastDonation'];

// Open a file to append the data
$file = fopen('data.csv', 'a');

// Write the data to the file
$data = array($name, $email, $bloodType, $phone, $dob, $lastDonation);
fputcsv($file, $data);

// Close the file
fclose($file);

// Redirect the user back to the form
header('Location: Blood Donor Registration.html');
?>
