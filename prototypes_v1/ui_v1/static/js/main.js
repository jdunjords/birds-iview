function checkPasswords()
{
   if (document.getElementById("inputPassword").value === document.getElementById("confirmedPassword").value)
   {
       alert("success");
   }
   else
   {
      alert("passwords dont match");
   }
}

