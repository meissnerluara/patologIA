
if(!point_in_rectangle(rect_student.left, rect_student.top, rect_teacher.left, rect_teacher.top, rect_teacher.right, rect_teacher.botton)) {
    
    ctx.strokeStyle='red';

    $.alert({
        title: 'Sorry',
        content: 'your answer did not come close to the expected result!',
        icon: 'fa fa-thumbs-down'
    });
}
else{

    ctx.strokeStyle='green';

    $.alert({
        title: 'Congratulations',
        content: 'your answer is correct!!',
        icon: 'fa fa-thumbs-up'
    });
}