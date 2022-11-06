const premiumCourses = document.querySelectorAll('.premiumCourse');
premiumCourses.forEach((premiumCourse)=>{
    premiumCourse.addEventListener('mouseover', ()=>{
        const premCourse = premiumCourse.querySelector('.main-heading');
        const fakeCourse = premiumCourse.querySelector('.fake-heading');
        premCourse.classList.add('d-none');
        fakeCourse.classList.remove('d-none');
    })
    premiumCourse.addEventListener('mouseleave', ()=>{
        const premCourse = premiumCourse.querySelector('.main-heading');
        const fakeCourse = premiumCourse.querySelector('.fake-heading');
        premCourse.classList.remove('d-none');
        fakeCourse.classList.add('d-none');
    })
})