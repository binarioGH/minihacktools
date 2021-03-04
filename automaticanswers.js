


//done-start - done-complete - done-retry



let video = document.getElementById("home_video_js");

let next = document.getElementsByClassName("FrameRight")[0];


video.addEventListener("ended", function(){next.click()});


let important_butts = document.getElementsByClassName("answer-choice-button");
let first = document.getElementsByClassName("done-start");
let retry = document.getElementsByClassName("done-retry");
let total = 0;

setInterval(function(){ 
	let next = document.getElementsByClassName("FrameRight")[0];
	important_butts = document.getElementsByClassName("answer-choice-button");
	let important = Array.prototype.slice.call(important_butts, 0);
	first = document.getElementsByClassName("done-start");
	retry = document.getElementsByClassName("done-retry");
	let a1 = Array.prototype.slice.call(first, 0);
	let a2 = Array.prototype.slice.call(retry, 0);
	let answers = a1.concat(a2);
	let total_questions = important.concat(answers);
	for(question of total_questions){
		question.click();
	}
	next.click();
}, 500);


/*


Assessment_Main_Body_Content_Question - test questions

*/