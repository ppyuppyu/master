//유효성 검사
function checkMember(){
    let form = doucment.regForm;
    let id = form.uid;
    let pw1 = form.pw1;
    let pw2 = form.pw2;

    if(id.value.length < 4){
        alert("아이디는 4~15자까지 가능합니다.");
        id.select();
        return false;
    
    }else{
        form.submit();
    }
}

let pw_pat1 = 
let pw_pat2

//console.log(pw1.value);
//console.log(pw_pat1.test(pw1.value));
if(id.value.length <4){
    alert("아이디는 4~15자까지 가능합니다.");
    id.select();
    return false;
}else if(MediaList.value == ""){
    alert("이메일은 필수 입력항목입니다.");
    MediaList.focus(); 
    return false;
}else if(pw1.value.length <8 || !pw)

}