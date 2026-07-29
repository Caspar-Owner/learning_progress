function score(marks){
    if(marks < 33) return "fail";
    else if(marks >= 33 && marks <= 59) return "grade-D";
    else if(marks >= 60 && marks <= 69) return "grade-C";
    else if(marks >= 70 && marks <= 89) return "grade-B";
    else if(marks >= 90 && marks <= 100) return "grade-A";
    else return "Invalid Marks 𛈄"
}
 
alok = score(300)
console.log(alok)