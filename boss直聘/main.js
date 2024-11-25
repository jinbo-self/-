
const https = require('https');

https.get('https://www.zhipin.com/web/common/security-js/c844dae4.js', (resp) => {
    let data = '';

    // 接收数据
    resp.on('data', (chunk) => {
        data += chunk;
    });

    // 完成响应
    resp.on('end', () => {
        const fs = require('fs');
        const vm = require('vm');
        
        // 读取 3ed4e8d8.js 文件
        // const scriptContent = fs.readFileSync('./JIAMI.js', 'utf-8');
        const scriptContent = data;
        // 创建一个新的 VM 上下文
        const context = {
            window: {},
            document: {},
            console: console,
            // 你可以在这里添加其他需要的全局对象
        };
        
        // 使用 vm 模块运行脚本
        vm.createContext(context); // 创建一个新的上下文
        vm.runInContext(scriptContent, context); // 执行脚本
        
        // 假设 3ed4e8d8.js 中定义了 ABC 类
        const ABC = context.window.ABC; // 获取 ABC 类
        
        // 创建 ABC 的实例
        const a = new ABC();
        t='mL1y9kivtFaalc8jzrAHbCQ9qqrJiOAlP17TrPYdqws='
        n="1732433999745"
        // 假设 z 是一个方法，并且它接受 x1 和 x2 作为参数
        const b = a.z(t, parseInt(n) + 60 * (480 + (new Date).getTimezoneOffset()) * 1e3); // 调用 z 方法
        const jiamihou = encodeURIComponent(b)
        
        console.log('Value of b:', b); // 输出 b 的值
        // console.log('Script Content:', data);
        // 这里可以执行获取的脚本
        // const context = { /* your context */ };
        // vm.runInContext(data, context);
    });

}).on('error', (err) => {
    console.log('Error: ' + err.message);
});


