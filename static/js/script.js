function EmailAuthentication(){
      var EmailValue=document.getElementById('emails').value;
      var error=document.getElementById('email_error');
      var button=document.getElementById('submitbtn');
      const emailpattern=/^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      error.textContent='';

      if(!emailpattern.test(EmailValue)){
        error.textContent="Please Enter a Valid Email(example@gmail.com)";
        button.type='button'
        if(EmailValue==''){
            error.textContent='';
          }
      }
      else
      {
        button.type='submit';
      }
}
// for phone number authentication
function MobileAuthentication(){
    var MobileValue=document.getElementById('phone').value;
    var errormessage=document.getElementById('mobile_error');
    var button=document.getElementById('submitbtn');
    const MobilePattern=/^03[0-9]{9}$/;

    errormessage.textContent='';

    if(!MobilePattern.test(MobileValue)){
      errormessage.textContent="Please Enter a Valid Mobile No(03365298230)";
      button.type='button'
      if(MobileValue==''){
        errormessage.textContent='';
      }
    }
    else
    {
      button.type='submit';
    }

}
// password authetication
function PasswordAuthentication()
{
    var PasswordValue=document.getElementById('SingUpPassword').value;
    var errormessage=document.getElementById('password_error');
    var button=document.getElementById('submitbtn');
    var PasswordPattern=/^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$/;

    errormessage.textContent='';

    if(!PasswordPattern.test(PasswordValue)){
      errormessage.textContent="Please Enter a Password atleast 6 character,one uppercase, one digit";
      button.type='button'
      if(PasswordValue==''){
        errormessage.textContent='';
      }
    }
    else
    {
      button.type='submit';
    }
}
// CONFIRM PASSWORD AUTHENTICATION
function ConfirmPassword(){
    var ConfirmPassword=document.getElementById('confirm-password').value;
    var PasswordValue=document.getElementById('SingUpPassword').value;
    var errormessage=document.getElementById('confirmpassword_error');
    var button=document.getElementById('submitbtn');
    errormessage.textContent='';

    if(ConfirmPassword!=PasswordValue && PasswordValue!=''){
      errormessage.textContent="Please Enter Same Password";
      button.type='button'
      if(ConfirmPassword==''){
        errormessage.textContent='';
      }
    }
    else if(PasswordValue==''){
        errormessage.textContent="Please Enter Password First";
        button.type='button'
        if(ConfirmPassword==''){
          errormessage.textContent='';
        }
    }
    else
    {
      button.type='submit';
    }
}