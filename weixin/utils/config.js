import EventEmitter from "./event-emitter";

let baseURL = 'https://movie.naturez.cn/api';
// baseURL = 'http://192.168.8.110:8820/api';

try {
    let res = wx.getSystemInfoSync();
    if (res.platform === 'devtools') {
        baseURL = 'http://127.0.0.1:8820/api';
    }
} catch (e) {
    // Do something when catch error
}

module.exports.baseURL = baseURL;

module.exports.apiMap = {
    login: '/passport/wx/login/',
    movie: '/movie/',
    detail: '/movie/detail/',
    tag: '/movie/tag/',
    retain: '/retain/'
};

module.exports.emitter = new EventEmitter();

module.exports.gData = {
    userSid: null,
    userInfo: null
};