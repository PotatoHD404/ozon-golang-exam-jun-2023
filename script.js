// codeforces parser

$x("/html/body/div[6]/div[4]/div[2]/div[2]/div[6]/table/tbody/tr/td[1]/a").map(el => ([el.innerText, el.href]))

let data1 = $x("/html/body/div[6]/div[4]/div[2]/div[3]/div[2]/div/div[5]/div[2]/div/pre").map(el => el.innerText);

let inputs = data1.filter((el, i) => i % 2 === 0)

let outputs = data1.filter((el, i) => i % 2 === 1)

// codeforces parser
let res = {};
(async ($x) => {
    let tasks = $x("/html/body/div[6]/div[4]/div[2]/div[2]/div[6]/table/tbody/tr/td[1]/a").map(el => ([el.innerText, el.href]))

    let win = window.open(tasks[0][1], `w1`)
    for (let i = 0; i < tasks.length; ++i) {
        let task = tasks[i];
        console.log(task)
        win.location = task[1];
        await new Promise(r => setTimeout(r, 5000));
        let data1 = $x("/html/body/div[6]/div/div[2]/div[3]/div[2]/div/div[5]/div[2]/div/pre", win.document).map(el => el.innerText);
        console.log(data1)
        let inputs = data1.filter((el, i) => i % 2 === 0)
        let outputs = data1.filter((el, i) => i % 2 === 1)
        res[task[0]] = []
        for (let i = 0; i < inputs.length; i++) {
            res[task[0]].push({input: inputs[i], output: outputs[i]})
        }
    }
})($x)


// yandex contest parser
let res = {};
(async ($x) => {
    let tasks = $x("/html/body/div[3]/div/ul[2]/li/a").map(el => [el.innerText.split('.')[0], el.href]);


    for (let i = 0; i < tasks.length; ++i) {
        let task = tasks[i];
        console.log(task)
        let win = window.open(task[1], `w1`)
        await new Promise(r => setTimeout(r, 1000));
        let inputs = $x("/html/body/div[3]/div/form/fieldset/div[1]/div/table/tbody/tr/td[1]/pre", win.document).map(el => el.innerText)
        let outputs = $x("/html/body/div[3]/div/form/fieldset/div[1]/div/table/tbody/tr/td[2]/pre", win.document).map(el => el.innerText)
        res[task[0]] = []
        for (let i = 0; i < inputs.length; i++) {
            res[task[0]].push({input: inputs[i], output: outputs[i]})
        }
    }
})($x)






