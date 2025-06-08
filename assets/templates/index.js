let currentApi = '/api/choose_start';
        let lastResult = "";

        // 全局保存已显示的成就
        let allAchievements = new Set();

        function updateUI(data) {
            let questionText = data.message || '';
            let resultText = '';
            let nextQuestion = '';

            // 判断是否有下一个问题
            if (questionText.includes('\n')) {
                // 找到第一个换行，把前面所有内容都当作结果，后面是下一个问题
                const idx = questionText.indexOf('\n');
                resultText = questionText.slice(0, idx).trim();
                nextQuestion = questionText.slice(idx + 1).trim();
                // 如果 nextQuestion 还有内容且下一行不是问题，则把所有多余行都归到 resultText
                if (nextQuestion && !nextQuestion.startsWith('>>>')) {
                    // 继续往下找下一个换行
                    const idx2 = nextQuestion.indexOf('\n');
                    if (idx2 !== -1) {
                        resultText += '\n' + nextQuestion.slice(0, idx2).trim();
                        nextQuestion = nextQuestion.slice(idx2 + 1).trim();
                    } else {
                        resultText += '\n' + nextQuestion;
                        nextQuestion = '';
                    }
                }
            } else {
                resultText = questionText;
                nextQuestion = '';
            }

            // 只在有新结果时更新 lastResult
            if (resultText) lastResult = resultText;

            document.getElementById('result').textContent = lastResult;
            document.getElementById('message').textContent = nextQuestion;

            const optionsDiv = document.getElementById('options');
            const bottomOptionsDiv = document.getElementById('bottom-options');
            optionsDiv.innerHTML = '';
            bottomOptionsDiv.innerHTML = '';

            if (data.options) {
                const bottomBtns = [];
                data.options.forEach((optionObj, idx) => {
                    if (
                        optionObj.text === '关于' ||
                        optionObj.text === '退出' ||
                        optionObj.text === '查看成就' ||
                        optionObj.text === '清除数据'
                    ) {
                        bottomBtns.push({option: optionObj.text, key: optionObj.key});
                    } else {
                        const button = document.createElement('button');
                        button.textContent = optionObj.text;
                        if (optionObj.text === '开始游戏') {
                            button.className = 'start-btn';
                        }
                        button.onclick = () => makeChoice(optionObj.key, data.start_event);
                        optionsDiv.appendChild(button);
                    }
                });
                // 渲染底部横排按钮
                bottomBtns.forEach(({option, key}) => {
                    const button = document.createElement('button');
                    button.textContent = option;
                    button.className = 'half-btn';
                    if (option === '关于') {
                        button.onclick = showAbout;
                    } else if (option === '退出') {
                        button.onclick = () => makeChoice(key, data.start_event);
                    } else if (option === '查看成就') {
                        button.onclick = showAchievements;
                    } else if (option === '清除数据') {
                        button.onclick = confirmClearData;
                    }
                    bottomOptionsDiv.appendChild(button);
                });
            }
            if (data.game_over) {
                const button = document.createElement('button');
                button.textContent = '重新开始';
                button.onclick = () => window.location.reload();
                optionsDiv.appendChild(button);
            }
            // 累积显示成就
            if (data.achievements) {
                const achievementsDiv = document.getElementById('achievements');
                const listDiv = document.getElementById('achievements-list');
                // 把新成就加入全局Set
                let hasNew = false;
                data.achievements.forEach(achievement => {
                    if (!allAchievements.has(achievement)) hasNew = true;
                    allAchievements.add(achievement);
                });
                // 只要有成就就渲染
                if (allAchievements.size > 0) {
                    listDiv.innerHTML = '';
                    Array.from(allAchievements).reverse().forEach(achievement => {
                        const p = document.createElement('p');
                        p.textContent = achievement;
                        listDiv.appendChild(p);
                    });
                    achievementsDiv.style.display = 'block';
                }
            }

            // 控制封面图片显示
            const coverImg = document.getElementById('cover-img');
            if (currentApi === '/api/choose_start') {
                coverImg.style.display = 'block';
            } else {
                coverImg.style.display = 'none';
            }
        }

        function makeChoice(choice, start_event=null) {
            let body = {};
            if (currentApi === '/api/choose_school') {
                body = { school: choice, start_event: start_event };
            } else if (start_event) {
                body = { choice: choice, start_event: start_event };
            } else {
                body = { choice: choice };
            }

            fetch(currentApi, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(body)
            })
            .then(response => response.json())
            .then (data => {
                updateUI(data);
                if (data.next_event === 'school_event') currentApi = '/api/school_event';
                else if (data.next_event === 'random_event') currentApi = '/api/random_event';
                else if (data.next_event === 'choose_school') currentApi = '/api/choose_school';
                else if (data.game_over) currentApi = '/api/choose_start';
            })
            .catch(error => console.error('Error:', error));
        }

        function showAchievements() {
            fetch('/api/get_achievements')
                .then(response => response.json())
                .then(data => {
                    let msg = "当前得分：" + data.score + "\n";
                    if (data.achievements.length > 0) {
                        msg += "已获得成就：\n" + data.achievements.join("\n");
                    } else {
                        msg += "还没有获得任何成就。";
                    }
                    alert(msg);
                });
        }

        function confirmClearData() {
            // 弹出确认页面
            if (confirm("确定要清除所有成就和分数吗？")) {
                fetch('/api/clear_data', {method: 'POST'})
                    .then(response => response.json())
                    .then(data => {
                        alert(data.message);
                    });
            }
        }

        function showAbout() {
            const aboutDiv = document.getElementById('about');
            aboutDiv.innerHTML = `<pre style="white-space:pre-line;">About OK School Life
Version 0.4
At home, May 30, 2025

Hi, I'm Stiil Alive, in Chinese “还活着”, the developer of this game.

First of all, thank you for playing this game.
This is a simple text-based game where you can choose your school life path.
You can make choices, earn achievements, and see how your decisions affect your story.
The game includes some lighthearted elements, as well as black humor elements.
Most of the content is based on my own school life experiences, so it may not be suitable for everyone.
And I'm trying to make it funnier, so there are some jokes in it.

I'm a newbie developer, and this is my first game.
To be honest, I don't know how to make a game. I just wanted to create a game that I would enjoy playing.
I must say that so many people have helped me a lot, including my friends and classmates.
They're WaiJade, lagency, 智心逍遥, sky, YaXuan, Tomato, GuoHao, and many others.
Especially, WaiJade, the co-developer of this game, wants to say something:

"I am WaiJade. 
Thanks for developing this game, which has reignited my passion for programming. 
I was primarily responsible for the script that automates the packaging of the game's executable file,
and contributed a little to the event library. 
Thank you for playing!"

I also want to thank the Modern AI Technology, especially OpenAI, 
for providing the tools and resources that made this game possible.
I'd like to thank Github for hosting the source code and allowing me to share it with everyone.

This game is open source, and you can find the source code on GitHub:
https://github.com/still-alive-hhz/OK-School-Life
The game is still in development, so there may be bugs or incomplete features.
If you have any questions or suggestions, please feel free to contact me.

Enjoy the game!</pre>
<button onclick="hideAbout()">返回</button>`;
            aboutDiv.style.display = 'block';
            document.getElementById('result').style.display = 'none';
            document.getElementById('message').style.display = 'none';
            document.getElementById('options').style.display = 'none';
            document.getElementById('achievements').style.display = 'none';
            document.getElementById('bottom-options').style.display = 'none'; // 新增：隐藏底部按钮
        }

        function hideAbout() {
            document.getElementById('about').style.display = 'none';
            document.getElementById('result').style.display = '';
            document.getElementById('message').style.display = '';
            document.getElementById('options').style.display = '';
            document.getElementById('achievements').style.display = '';
            document.getElementById('bottom-options').style.display = ''; // 新增：恢复底部按钮
        }

        // 关键：页面加载时自动请求
        window.onload = function() {
            fetch('/api/start_game')
                .then(response => response.json())
                .then(data => updateUI(data));
        };