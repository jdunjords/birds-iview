function checkPasswords()
{

   if (document.getElementsByName("inputPassword") !== document.getElementsByName("confirmedPassword"))
   {
       alert("passwords dont match")
       document.getElementById("failedResponse").innerHTML = "passwords do not match"
   }
}
