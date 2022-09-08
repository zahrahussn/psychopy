/******************************* 
 * Diacriticstwowordtasks Test *
 *******************************/


// store info about the experiment session:
let expName = 'diacriticsTwoWordTasks';  // from the Builder filename that created this script
let expInfo = {'participant': ''};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0.6549, 0.6549, 0.6549]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const taskOrderLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(taskOrderLoopBegin(taskOrderLoopScheduler));
flowScheduler.add(taskOrderLoopScheduler);
flowScheduler.add(taskOrderLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'PracticeArb.xlsx', 'path': 'PracticeArb.xlsx'},
    {'name': 'LDPractice.png', 'path': 'LDPractice.png'},
    {'name': 'LDWordList.xlsx', 'path': 'LDWordList.xlsx'},
    {'name': 'noiseRect.png', 'path': 'noiseRect.png'},
    {'name': 'SDInst2.png', 'path': 'SDInst2.png'},
    {'name': 'SDWordList.xlsx', 'path': 'SDWordList.xlsx'},
    {'name': 'LDInst2.png', 'path': 'LDInst2.png'},
    {'name': 'CommonInst.png', 'path': 'CommonInst.png'},
    {'name': 'TaskOrder.xlsx', 'path': 'TaskOrder.xlsx'},
    {'name': 'LDInst1.png', 'path': 'LDInst1.png'},
    {'name': 'Reminder.png', 'path': 'Reminder.png'},
    {'name': 'SDPractice.png', 'path': 'SDPractice.png'},
    {'name': 'SDInst1.png', 'path': 'SDInst1.png'},
    {'name': 'SD_PracticeArb.xlsx', 'path': 'SD_PracticeArb.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.0';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var taskOrderCodeClock;
var CommonInst1;
var CommonInstResp1;
var innitialCodeClock;
var randint;
var list_Dist;
var fontsize;
var LDInst1Clock;
var LDInst_1;
var LDInst1Resp;
var LDInst2Clock;
var LDInst_2;
var LDInst2Resp;
var LDPracticeInstClock;
var practiceInst;
var practiceInstResp;
var fixationInstClock;
var fixationInst_1;
var fixationInstResp;
var LDPracticeClock;
var xstim1_D;
var ystim1_D;
var stim1_D;
var fixation;
var noiseImage;
var noiseImage_D;
var wordPractice;
var distWord;
var cue;
var PracticeResponse;
var LDPRacticeResponseClock;
var soundfile;
var feedback;
var taskInstClock;
var LDTaskResp;
var LDInstructrions;
var LDInstructionArb;
var LDTaskClock;
var fixation_2;
var noiseImage_2;
var noiseImage_D_2;
var LDWord_1;
var distWord_2;
var cue_2;
var LDResponse;
var LDResponse_2Clock;
var feedback_2;
var LDBreakClock;
var LDBreakResp;
var endOfLD;
var endOfLDArb;
var SDInitalCodeClock;
var SDlist_limit;
var SDword1_Dist;
var SDword2_Dist;
var SDInst1Clock;
var SDInst_1;
var SDInst1Resp;
var SDInst2Clock;
var SDInst_2;
var SDInst2Resp;
var SDPracticeInstClock;
var SDPractiveInst_1;
var SDPracticeInstResp;
var fixationInst_4Clock;
var fixationInst_5;
var fixationInst4Resp;
var SDPracticeClock;
var stim1;
var stim2;
var xstim1;
var ystim1;
var xstim2;
var ystim2;
var stim2_D;
var xstim2_D;
var ysim2_D;
var SDFixation;
var SDPracticeWord1;
var SDPracticeDist1;
var cue_3;
var noiseImage_3;
var noiseImage_D_3;
var SDPracticeWord2;
var SDPracticeDist2;
var cue_6;
var SDPracticeResp;
var SDPracticeResponseClock;
var feedback_3;
var SDTaskInstClock;
var SDTaskResp;
var SDInstructrions;
var SDInstructionArb;
var SDTaskClock;
var SDFixation_2;
var SDWord1;
var SDDist1;
var cue_4;
var noiseImage_4;
var noiseImage_D_4;
var SDWord2;
var SDDist2;
var cue_5;
var SDResp;
var SDResponseClock;
var feedback_4;
var SDBreakClock;
var SDBreakResp;
var endOfSD;
var endOfSDArb;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "taskOrderCode"
  taskOrderCodeClock = new util.Clock();
  /* Syntax Error: Fix Python code */
  CommonInst1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'CommonInst1', units : undefined, 
    image : 'CommonInst.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.5, 0.9],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  CommonInstResp1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "innitialCode"
  innitialCodeClock = new util.Clock();
  randint = function(min, maxplusone) {
    return Math.floor((Math.random() * (maxplusone - min) )) + min;
  }
  
  /* The randint() function on python includes the lower limit and excludes the upper limit,
  i.e.: (0,3) would yiled three numbers: 0, 1, 2. 
  When it is converting it to Javascript, it includes the upper limit,
  i.e.: (0,3) would yield 4 numbers: 0, 1, 2, 3. 
  This code component changes the conversion to Javascript, in order for it to match python.*/
  list_Dist = ["\u0634\u0631\u064a\u0641", "\u0634\u064e\u0631\u0650\u064a\u0641\u064c", "\u062d\u0632\u064a\u0646", "\u062d\u064e\u0632\u0650\u064a\u0646\u064d", "\u0633\u0624\u0627\u0644", "\u0633\u064f\u0624\u0652\u0627\u0644\u064f", "\u0646\u0635\u0648\u0635", "\u0646\u064f\u0635\u064f\u0648\u0635\u064c", "\u062d\u0642\u0648\u0642", "\u062d\u064f\u0642\u064f\u0648\u0642\u064e", "\u0639\u0645\u064a\u062f", "\u0639\u064e\u0645\u0650\u064a\u062f\u0627\u064b", "\u062c\u0631\u064a\u062d\u0629", "\u062c\u064e\u0631\u0650\u064a\u062d\u064e\u0629", "\u0625\u0646\u0634\u0627\u0621", "\u0625\u0650\u0646\u0652\u0634\u064e\u0627\u0621", "\u0645\u062a\u0631\u0648\u0643", "\u0645\u064e\u062a\u0652\u0631\u064f\u0648\u0643", "\u0645\u0639\u062f\u0648\u062f", "\u0645\u064e\u0639\u0652\u062f\u064f\u0648\u062f", "\u0623\u0633\u0631\u0627\u0631", "\u0623\u064e\u0633\u0652\u0631\u064e\u0627\u0631", "\u0645\u0641\u0639\u0648\u0644", "\u0645\u064e\u0641\u0652\u0639\u064f\u0648\u0644", "\u0643\u062a\u0627\u0628", "\u0643\u0650\u062a\u064e\u0627\u0628\u064c", "\u062a\u0623\u062c\u064a\u0631", "\u062a\u064e\u0623\u0652\u062c\u0650\u064a\u0631", "\u062a\u0627\u0631\u0643", "\u062a\u064e\u0627\u0631\u0650\u0643\u0627\u064b", "\u0633\u0639\u064a\u062f", "\u0633\u064e\u0639\u0650\u064a\u062f\u064f", "\u0625\u062c\u0631\u0627\u0645", "\u0625\u0650\u062c\u0652\u0631\u064e\u0627\u0645", "\u0645\u062f\u0631\u0648\u0633", "\u0645\u064e\u062f\u0652\u0631\u064f\u0648\u0633", "\u062a\u0642\u0644\u064a\u0628", "\u062a\u064e\u0642\u0652\u0644\u0650\u064a\u0628", "\u0637\u0631\u064a\u0642", "\u0637\u064e\u0631\u0650\u064a\u0642\u064e", "\u062c\u0645\u064a\u0644", "\u062c\u064e\u0645\u0650\u064a\u0644\u064f", "\u0625\u0646\u0633\u0627\u0646", "\u0625\u0650\u0646\u0652\u0633\u064e\u0627\u0646", "\u0625\u062c\u0627\u0628\u0629", "\u0625\u0650\u062c\u0627\u0628\u064e\u0629\u064c", "\u0645\u0648\u0642\u0648\u0641", "\u0645\u064e\u0648\u0652\u0642\u064f\u0648\u0641", "\u062f\u0631\u0648\u0633", "\u062f\u064f\u0631\u064f\u0648\u0633\u064e", "\u0645\u0645\u0646\u0648\u0646", "\u0645\u064e\u0645\u0652\u0646\u064f\u0648\u0646", "\u0639\u0627\u0631\u0641", "\u0639\u064e\u0627\u0631\u0650\u0641\u064c", "\u0633\u0631\u064a\u0639", "\u0633\u064e\u0631\u0650\u064a\u0639\u064f", "\u0643\u0631\u064a\u0645\u0629", "\u0643\u064e\u0631\u0650\u064a\u0645\u064e\u0629", "\u0623\u0648\u0644\u0627\u062f ", "\u0623\u064e\u0648\u0652\u0644\u064e\u0627\u062f", "\u0644\u0645\u0627\u0646", "\u0644\u064e\u0645\u064e\u0627\u0646\u0652", "\u0634\u0645\u0627\u0646", "\u0634\u064e\u0645\u064e\u0627\u0646\u064f", "\u0633\u0642\u0648\u0642", "\u0633\u064f\u0642\u064f\u0648\u0642\u064f", "\u0645\u062c\u0642\u0648\u062d", "\u0645\u064e\u062c\u0652\u0642\u0648\u062d\u0652", "\u0645\u062c\u0642\u0648\u0644", "\u0645\u064e\u062c\u0642\u064f\u0648\u0644\u064c", "\u0634\u062f\u064a\u0641", "\u0634\u064e\u062f\u0652\u064a\u0641\u064f", "\u0623\u0635\u0631\u062c", "\u0623\u064e\u0635\u0631\u064e\u062c\u064f", "\u0623\u0635\u0631\u0636", "\u0623\u064e\u0635\u0652\u0631\u064e\u0636", "\u0623\u062c\u063a\u0631", "\u0623\u064e\u062c\u0652\u063a\u064e\u0631", "\u0633\u0644\u0627\u062f", "\u0633\u064e\u0644\u064e\u0627\u062f\u0652", "\u0639\u0644\u0627\u062f", "\u0639\u064e\u0644\u0652\u0627\u062f\u0650", "\u0631\u0645\u0648\u0639", "\u0631\u064f\u0645\u064f\u0648\u0639\u064f", "\u0642\u0627\u062f\u0644", "\u0642\u064e\u0627\u062f\u0650\u0644\u064f", "\u0642\u0648\u062f\u0644", "\u0642\u064f\u0648\u062f\u064e\u0644\u064e", "\u062d\u0648\u0636\u0648\u0639", "\u062d\u064f\u0648\u0636\u064f\u0648\u0639\u0650", "\u0636\u0638\u0631\u0645", "\u0636\u064e\u0638\u0652\u0631\u064e\u0645", "\u0636\u0639\u0631\u0645", "\u0636\u064e\u0639\u0652\u0631\u064e\u0645", "\u0630\u062b\u0644\u0642", "\u0630\u064e\u062b\u0644\u064f\u0642\u064f", "\u0647\u062a\u062b\u0645\u0639", "\u0647\u064e\u062a\u062b\u064e\u0645\u064e\u0639", "\u0645\u062a\u062b\u0645\u0639", "\u0645\u064f\u062a\u064e\u062b\u0645\u0650\u0639", "\u0631\u0633\u0644\u0628\u0642", "\u0631\u064e\u0633\u064f\u0644\u0628\u0650\u0642", "\u0642\u063a\u0631\u0635\u0630", "\u0642\u064e\u063a\u0631\u064e\u0635\u064f\u0630", "\u0642\u063a\u062c\u0635\u0630", "\u0642\u064f\u063a\u062c\u064f\u0635\u0652\u0630", "\u0634\u0644\u0628\u0641\u0631", "\u0634\u064f\u0644\u0628\u064e\u0641\u064f\u0631", "\u0641\u0628\u062f\u0635", "\u0641\u064f\u0628\u062f\u064e\u0635\u0650", "\u0641\u0628\u062f\u062b", "\u0641\u064f\u0628\u0652\u062f\u064e\u062b", "\u0646\u0645\u062a\u0642", "\u0646\u064e\u0645\u062a\u064f\u0642\u064e", "\u062b\u0637\u0644\u062f\u0645", "\u062b\u064e\u0637\u064e\u0644\u062f\u064f\u0645", "\u0644\u0646\u0638\u0643", "\u0644\u064e\u0646\u0638\u064e\u0643\u0650", "\u0643\u0646\u0647\u0642\u0629", "\u0643\u064e\u0646\u0650\u0647\u0642\u064e\u0629"];
  fontsize = 0.2;
  
  // Initialize components for Routine "LDInst1"
  LDInst1Clock = new util.Clock();
  LDInst_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'LDInst_1', units : undefined, 
    image : 'LDInst1.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.5, 0.9],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  LDInst1Resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "LDInst2"
  LDInst2Clock = new util.Clock();
  LDInst_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'LDInst_2', units : undefined, 
    image : 'LDInst2.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.5, 0.9],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  LDInst2Resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "LDPracticeInst"
  LDPracticeInstClock = new util.Clock();
  practiceInst = new visual.ImageStim({
    win : psychoJS.window,
    name : 'practiceInst', units : undefined, 
    image : 'LDPractice.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.5, 0.9],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  practiceInstResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixationInst"
  fixationInstClock = new util.Clock();
  fixationInst_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixationInst_1', units : undefined, 
    image : 'Reminder.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.5, 0.9],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  fixationInstResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "LDPractice"
  LDPracticeClock = new util.Clock();
  xstim1_D = "";
  ystim1_D = "";
  stim1_D = "";
  
  fixation = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation', 
    vertices: 'cross', size:[0.04, 0.04],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  noiseImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'noiseImage', units : undefined, 
    image : 'noiseRect.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  noiseImage_D = new visual.ImageStim({
    win : psychoJS.window,
    name : 'noiseImage_D', units : undefined, 
    image : 'noiseRect.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  wordPractice = new visual.TextStim({
    win: psychoJS.window,
    name: 'wordPractice',
    text: '',
    font: 'Courier',
    units: undefined, 
    pos: [0, 0], height: fontsize,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  distWord = new visual.TextStim({
    win: psychoJS.window,
    name: 'distWord',
    text: '',
    font: 'Courier',
    units: undefined, 
    pos: [0, 0], height: fontsize,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  cue = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cue', 
    vertices: [[-[0.65, 3][0]/2.0, 0], [+[0.65, 3][0]/2.0, 0]],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  PracticeResponse = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "LDPRacticeResponse"
  LDPRacticeResponseClock = new util.Clock();
  soundfile = [800, 400];
  
  feedback = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.03,
    });
  feedback.setVolume(1.0);
  // Initialize components for Routine "taskInst"
  taskInstClock = new util.Clock();
  LDTaskResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  LDInstructrions = new visual.TextStim({
    win: psychoJS.window,
    name: 'LDInstructrions',
    text: 'You will now start the experimental block. \n\nPlease answer as quickly and as accurately as possible.\n\nPress space to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.4), (- 0.15)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  LDInstructionArb = new visual.TextStim({
    win: psychoJS.window,
    name: 'LDInstructionArb',
    text: 'ستبدأ الآن التجربة الفعلية ضمن هذه المجموعة\n\nيرجى الإجابة بسرعة و بدقة\n\nاضغط على شريط المسافة للمتابعة\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.4, 0.15], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "LDTask"
  LDTaskClock = new util.Clock();
  /* Syntax Error: Fix Python code */
  fixation_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_2', 
    vertices: 'cross', size:[0.04, 0.04],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  noiseImage_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'noiseImage_2', units : undefined, 
    image : 'noiseRect.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  noiseImage_D_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'noiseImage_D_2', units : undefined, 
    image : 'noiseRect.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  LDWord_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'LDWord_1',
    text: '',
    font: 'Courier',
    units: undefined, 
    pos: [0, 0], height: fontsize,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  distWord_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'distWord_2',
    text: '',
    font: 'Courier',
    units: undefined, 
    pos: [0, 0], height: fontsize,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  cue_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cue_2', 
    vertices: [[-[0.65, 3][0]/2.0, 0], [+[0.65, 3][0]/2.0, 0]],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  LDResponse = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "LDResponse_2"
  LDResponse_2Clock = new util.Clock();
  soundfile = [800, 400];
  
  feedback_2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.03,
    });
  feedback_2.setVolume(1.0);
  // Initialize components for Routine "LDBreak"
  LDBreakClock = new util.Clock();
  LDBreakResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  endOfLD = new visual.TextStim({
    win: psychoJS.window,
    name: 'endOfLD',
    text: 'You have completed this experimental block. \nPlease DO NOT press Esc or close the tab while taking a break.\nWhen you are ready, press Space to continue.\n',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.4), (- 0.15)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  endOfLDArb = new visual.TextStim({
    win: psychoJS.window,
    name: 'endOfLDArb',
    text: 'إنتهت هذه المجموعة.\nلا تغلق الصفحة و لا تضغط على مفتاح Escape.\nعندما تصبح جاهزاً، اضغط على شريط المسلفة (Space) للمتاعة.',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, 0.15], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "SDInitalCode"
  SDInitalCodeClock = new util.Clock();
  SDlist_limit = 60;
  SDword1_Dist = ["\u0623\u0633\u0639\u062f", "\u0623\u0633\u0639\u062f", "\u0623\u0633\u0639\u062f", "\u0623\u0633\u0639\u062f", "\u0623\u0633\u0639\u062f", "\u0623\u062e\u0631\u062c", "\u0623\u062e\u0631\u062c", "\u0623\u062e\u0631\u062c", "\u0623\u062e\u0631\u062c", "\u0623\u062e\u0631\u062c", "\u0642\u0627\u0626\u0644", "\u0642\u0627\u0626\u0644", "\u0642\u0627\u0626\u0644", "\u0642\u0627\u0626\u0644", "\u0642\u0627\u0626\u0644", "\u0635\u0631\u064a\u062d", "\u0635\u0631\u064a\u062d", "\u0635\u0631\u064a\u062d", "\u0635\u0631\u064a\u062d", "\u0635\u0631\u064a\u062d", "\u0645\u0642\u0627\u0644\u0629", "\u0645\u0642\u0627\u0644\u0629", "\u0645\u0642\u0627\u0644\u0629", "\u0645\u0642\u0627\u0644\u0629", "\u0645\u0642\u0627\u0644\u0629", "\u0627\u0639\u062a\u062f\u0649", "\u0627\u0639\u062a\u062f\u0649", "\u0627\u0639\u062a\u062f\u0649", "\u0627\u0639\u062a\u062f\u0649", "\u0627\u0639\u062a\u062f\u0649", "\u0633\u0645\u0627\u062d", "\u0633\u0645\u0627\u062d", "\u0633\u0645\u0627\u062d", "\u0633\u0645\u0627\u062d", "\u0633\u0645\u0627\u062d", "\u0623\u062f\u0627\u0646", "\u0623\u062f\u0627\u0646", "\u0623\u062f\u0627\u0646", "\u0623\u062f\u0627\u0646", "\u0623\u062f\u0627\u0646", "\u0623\u0631\u0639\u0628", "\u0623\u0631\u0639\u0628", "\u0623\u0631\u0639\u0628", "\u0623\u0631\u0639\u0628", "\u0623\u0631\u0639\u0628", "\u0623\u062c\u0628\u0631", "\u0623\u062c\u0628\u0631", "\u0623\u062c\u0628\u0631", "\u0623\u062c\u0628\u0631", "\u0623\u062c\u0628\u0631", "\u0623\u0633\u0644\u0645", "\u0623\u0633\u0644\u0645", "\u0623\u0633\u0644\u0645", "\u0623\u0633\u0644\u0645", "\u0623\u0633\u0644\u0645", "\u0631\u062c\u0648\u0639", "\u0631\u062c\u0648\u0639", "\u0631\u062c\u0648\u0639", "\u0631\u062c\u0648\u0639", "\u0631\u062c\u0648\u0639"];
  SDword2_Dist = ["\u0623\u0648\u0639\u062f", "\u0645\u0633\u0639\u0648\u062f", "\u0645\u062d\u0648\u0644", "\u0623\u0633\u0639\u062f", "\u0623\u0633\u0639\u062f", "\u0623\u0639\u0631\u062c", "\u062e\u0627\u0631\u062c", "\u0645\u0633\u0623\u0644\u0629", "\u0623\u062e\u0631\u062c", "\u0623\u062e\u0631\u062c", "\u0642\u0627\u0626\u0645", "\u064a\u0642\u0648\u0644", "\u062a\u0631\u0627\u062b", "\u0642\u0627\u0626\u0644", "\u0642\u0627\u0626\u0644", "\u062c\u0631\u064a\u062d", "\u0635\u0627\u0631\u062d", "\u0645\u0639\u0631\u0636", "\u0635\u0631\u064a\u062d", "\u0635\u0631\u064a\u062d", "\u0645\u062d\u0627\u0644\u0629", "\u064a\u0642\u0648\u0644\u0648\u0646", "\u0639\u0635\u0627\u0641\u064a\u0631", "\u0645\u0642\u0627\u0644\u0629", "\u0645\u0642\u0627\u0644\u0629", "\u0627\u0631\u062a\u062f\u0649", "\u0639\u062f\u0627\u0648\u0629", "\u062d\u0642\u064a\u0628\u0629", "\u0627\u0639\u062a\u062f\u0649", "\u0627\u0639\u062a\u062f\u0649", "\u0633\u0644\u0627\u062d", "\u0633\u0627\u0645\u062d", "\u0642\u0627\u062a\u0644", "\u0633\u0645\u0627\u062d", "\u0633\u0645\u0627\u062d", "\u0623\u0628\u0627\u0646", "\u0645\u062f\u064a\u0646", "\u0634\u0639\u0648\u0631", "\u0623\u062f\u0627\u0646", "\u0623\u062f\u0627\u0646", "\u0623\u0631\u0643\u0628", "\u0645\u0631\u0639\u0628", "\u0633\u0627\u0639\u062f", "\u0623\u0631\u0639\u0628", "\u0623\u0631\u0639\u0628", "\u0623\u062f\u0628\u0631", "\u0645\u062c\u0628\u0631", "\u0631\u0627\u062d\u0644", "\u0623\u062c\u0628\u0631", "\u0623\u062c\u0628\u0631", "\u0623\u0639\u0644\u0645", "\u0633\u0627\u0644\u0645", "\u0631\u0627\u062c\u0639", "\u0623\u0633\u0644\u0645", "\u0623\u0633\u0644\u0645", "\u0631\u0643\u0648\u0639", "\u0623\u0631\u062c\u0639", "\u0642\u0627\u0631\u0626", "\u0631\u062c\u0648\u0639", "\u0631\u062c\u0648\u0639"];
  fontsize = 0.2;
  
  // Initialize components for Routine "SDInst1"
  SDInst1Clock = new util.Clock();
  SDInst_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SDInst_1', units : undefined, 
    image : 'SDInst1.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.5, 0.9],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  SDInst1Resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SDInst2"
  SDInst2Clock = new util.Clock();
  SDInst_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SDInst_2', units : undefined, 
    image : 'SDInst2.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.5, 0.9],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  SDInst2Resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SDPracticeInst"
  SDPracticeInstClock = new util.Clock();
  SDPractiveInst_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'SDPractiveInst_1', units : undefined, 
    image : 'SDPractice.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.5, 0.9],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  SDPracticeInstResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixationInst_4"
  fixationInst_4Clock = new util.Clock();
  fixationInst_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixationInst_5', units : undefined, 
    image : 'Reminder.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.5, 0.9],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  fixationInst4Resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SDPractice"
  SDPracticeClock = new util.Clock();
  stim1 = "";
  stim2 = "";
  xstim1 = "";
  ystim1 = "";
  xstim2 = "";
  ystim2 = "";
  stim1_D = "";
  stim2_D = "";
  xstim1_D = "";
  ystim1_D = "";
  xstim2_D = "";
  ysim2_D = "";
  
  SDFixation = new visual.ShapeStim ({
    win: psychoJS.window, name: 'SDFixation', 
    vertices: 'cross', size:[0.04, 0.04],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  SDPracticeWord1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'SDPracticeWord1',
    text: '',
    font: 'Courier',
    units: undefined, 
    pos: [0, 0], height: fontsize,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  SDPracticeDist1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'SDPracticeDist1',
    text: '',
    font: 'Courier',
    units: undefined, 
    pos: [0, 0], height: fontsize,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  cue_3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cue_3', 
    vertices: [[-[0.65, 3][0]/2.0, 0], [+[0.65, 3][0]/2.0, 0]],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  noiseImage_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'noiseImage_3', units : undefined, 
    image : 'noiseRect.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  noiseImage_D_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'noiseImage_D_3', units : undefined, 
    image : 'noiseRect.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  SDPracticeWord2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'SDPracticeWord2',
    text: '',
    font: 'Courier',
    units: undefined, 
    pos: [0, 0], height: fontsize,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  SDPracticeDist2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'SDPracticeDist2',
    text: '',
    font: 'Courier',
    units: undefined, 
    pos: [0, 0], height: fontsize,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  cue_6 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cue_6', 
    vertices: [[-[0.65, 3][0]/2.0, 0], [+[0.65, 3][0]/2.0, 0]],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -9, interpolate: true,
  });
  
  SDPracticeResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SDPracticeResponse"
  SDPracticeResponseClock = new util.Clock();
  soundfile = [800, 400];
  
  feedback_3 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.03,
    });
  feedback_3.setVolume(1.0);
  // Initialize components for Routine "SDTaskInst"
  SDTaskInstClock = new util.Clock();
  SDTaskResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  SDInstructrions = new visual.TextStim({
    win: psychoJS.window,
    name: 'SDInstructrions',
    text: 'You will now start the experimental block. \n\nPlease answer as quickly and as accurately as possible.\n\nPress space to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.4), (- 0.15)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  SDInstructionArb = new visual.TextStim({
    win: psychoJS.window,
    name: 'SDInstructionArb',
    text: 'ستبدأ الآن التجربة الفعلية ضمن هذه المجموعة\n\nيرجى الإجابة بسرعة و بدقة\n\nاضغط على شريط المسافة للمتابعة\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.4, 0.15], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "SDTask"
  SDTaskClock = new util.Clock();
  stim1 = "";
  stim2 = "";
  xstim1 = "";
  ystim1 = "";
  xstim2 = "";
  ystim2 = "";
  stim1_D = "";
  stim2_D = "";
  xstim1_D = "";
  ystim1_D = "";
  xstim2_D = "";
  ysim2_D = "";
  
  SDFixation_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'SDFixation_2', 
    vertices: 'cross', size:[0.04, 0.04],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  SDWord1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'SDWord1',
    text: '',
    font: 'Courier',
    units: undefined, 
    pos: [0, 0], height: fontsize,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  SDDist1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'SDDist1',
    text: '',
    font: 'Courier',
    units: undefined, 
    pos: [0, 0], height: fontsize,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  cue_4 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cue_4', 
    vertices: [[-[0.65, 3][0]/2.0, 0], [+[0.65, 3][0]/2.0, 0]],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  noiseImage_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'noiseImage_4', units : undefined, 
    image : 'noiseRect.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  noiseImage_D_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'noiseImage_D_4', units : undefined, 
    image : 'noiseRect.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  SDWord2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'SDWord2',
    text: '',
    font: 'Courier',
    units: undefined, 
    pos: [0, 0], height: fontsize,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  SDDist2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'SDDist2',
    text: '',
    font: 'Courier',
    units: undefined, 
    pos: [0, 0], height: fontsize,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  cue_5 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cue_5', 
    vertices: [[-[0.65, 3][0]/2.0, 0], [+[0.65, 3][0]/2.0, 0]],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -9, interpolate: true,
  });
  
  SDResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SDResponse"
  SDResponseClock = new util.Clock();
  soundfile = [800, 400];
  
  feedback_4 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.03,
    });
  feedback_4.setVolume(1.0);
  // Initialize components for Routine "SDBreak"
  SDBreakClock = new util.Clock();
  SDBreakResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  endOfSD = new visual.TextStim({
    win: psychoJS.window,
    name: 'endOfSD',
    text: 'You have completed this experimental block. \nPlease DO NOT press Esc or close the tab while taking a break.\nWhen you are ready, press Space to continue.\n',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.4), (- 0.15)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  endOfSDArb = new visual.TextStim({
    win: psychoJS.window,
    name: 'endOfSDArb',
    text: 'إنتهت هذه المجموعة.\nلا تغلق الصفحة و لا تضغط على مفتاح Escape.\nعندما تصبح جاهزاً، اضغط على شريط المسلفة (Space) للمتاعة.',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, 0.15], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var taskOrder;
var currentLoop;
function taskOrderLoopBegin(taskOrderLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    taskOrder = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'TaskOrder.xlsx',
      seed: undefined, name: 'taskOrder'
    });
    psychoJS.experiment.addLoop(taskOrder); // add the loop to the experiment
    currentLoop = taskOrder;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    taskOrder.forEach(function() {
      const snapshot = taskOrder.getSnapshot();
    
      taskOrderLoopScheduler.add(importConditions(snapshot));
      taskOrderLoopScheduler.add(taskOrderCodeRoutineBegin(snapshot));
      taskOrderLoopScheduler.add(taskOrderCodeRoutineEachFrame());
      taskOrderLoopScheduler.add(taskOrderCodeRoutineEnd());
      const LDTaskOrderLoopScheduler = new Scheduler(psychoJS);
      taskOrderLoopScheduler.add(LDTaskOrderLoopBegin(LDTaskOrderLoopScheduler, snapshot));
      taskOrderLoopScheduler.add(LDTaskOrderLoopScheduler);
      taskOrderLoopScheduler.add(LDTaskOrderLoopEnd);
      const SDTaskOrderLoopScheduler = new Scheduler(psychoJS);
      taskOrderLoopScheduler.add(SDTaskOrderLoopBegin(SDTaskOrderLoopScheduler, snapshot));
      taskOrderLoopScheduler.add(SDTaskOrderLoopScheduler);
      taskOrderLoopScheduler.add(SDTaskOrderLoopEnd);
      taskOrderLoopScheduler.add(endLoopIteration(taskOrderLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var LDTaskOrder;
function LDTaskOrderLoopBegin(LDTaskOrderLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    LDTaskOrder = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nRepsTask1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'LDTaskOrder'
    });
    psychoJS.experiment.addLoop(LDTaskOrder); // add the loop to the experiment
    currentLoop = LDTaskOrder;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    LDTaskOrder.forEach(function() {
      const snapshot = LDTaskOrder.getSnapshot();
    
      LDTaskOrderLoopScheduler.add(importConditions(snapshot));
      LDTaskOrderLoopScheduler.add(innitialCodeRoutineBegin(snapshot));
      LDTaskOrderLoopScheduler.add(innitialCodeRoutineEachFrame());
      LDTaskOrderLoopScheduler.add(innitialCodeRoutineEnd());
      LDTaskOrderLoopScheduler.add(LDInst1RoutineBegin(snapshot));
      LDTaskOrderLoopScheduler.add(LDInst1RoutineEachFrame());
      LDTaskOrderLoopScheduler.add(LDInst1RoutineEnd());
      LDTaskOrderLoopScheduler.add(LDInst2RoutineBegin(snapshot));
      LDTaskOrderLoopScheduler.add(LDInst2RoutineEachFrame());
      LDTaskOrderLoopScheduler.add(LDInst2RoutineEnd());
      LDTaskOrderLoopScheduler.add(LDPracticeInstRoutineBegin(snapshot));
      LDTaskOrderLoopScheduler.add(LDPracticeInstRoutineEachFrame());
      LDTaskOrderLoopScheduler.add(LDPracticeInstRoutineEnd());
      LDTaskOrderLoopScheduler.add(fixationInstRoutineBegin(snapshot));
      LDTaskOrderLoopScheduler.add(fixationInstRoutineEachFrame());
      LDTaskOrderLoopScheduler.add(fixationInstRoutineEnd());
      const practiceTrialLoopScheduler = new Scheduler(psychoJS);
      LDTaskOrderLoopScheduler.add(practiceTrialLoopBegin(practiceTrialLoopScheduler, snapshot));
      LDTaskOrderLoopScheduler.add(practiceTrialLoopScheduler);
      LDTaskOrderLoopScheduler.add(practiceTrialLoopEnd);
      LDTaskOrderLoopScheduler.add(taskInstRoutineBegin(snapshot));
      LDTaskOrderLoopScheduler.add(taskInstRoutineEachFrame());
      LDTaskOrderLoopScheduler.add(taskInstRoutineEnd());
      const LDTrialLoopScheduler = new Scheduler(psychoJS);
      LDTaskOrderLoopScheduler.add(LDTrialLoopBegin(LDTrialLoopScheduler, snapshot));
      LDTaskOrderLoopScheduler.add(LDTrialLoopScheduler);
      LDTaskOrderLoopScheduler.add(LDTrialLoopEnd);
      LDTaskOrderLoopScheduler.add(LDBreakRoutineBegin(snapshot));
      LDTaskOrderLoopScheduler.add(LDBreakRoutineEachFrame());
      LDTaskOrderLoopScheduler.add(LDBreakRoutineEnd());
      LDTaskOrderLoopScheduler.add(endLoopIteration(LDTaskOrderLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var practiceTrial;
function practiceTrialLoopBegin(practiceTrialLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceTrial = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'PracticeArb.xlsx',
      seed: undefined, name: 'practiceTrial'
    });
    psychoJS.experiment.addLoop(practiceTrial); // add the loop to the experiment
    currentLoop = practiceTrial;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practiceTrial.forEach(function() {
      const snapshot = practiceTrial.getSnapshot();
    
      practiceTrialLoopScheduler.add(importConditions(snapshot));
      practiceTrialLoopScheduler.add(LDPracticeRoutineBegin(snapshot));
      practiceTrialLoopScheduler.add(LDPracticeRoutineEachFrame());
      practiceTrialLoopScheduler.add(LDPracticeRoutineEnd());
      practiceTrialLoopScheduler.add(LDPRacticeResponseRoutineBegin(snapshot));
      practiceTrialLoopScheduler.add(LDPRacticeResponseRoutineEachFrame());
      practiceTrialLoopScheduler.add(LDPRacticeResponseRoutineEnd());
      practiceTrialLoopScheduler.add(endLoopIteration(practiceTrialLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practiceTrialLoopEnd() {
  psychoJS.experiment.removeLoop(practiceTrial);

  return Scheduler.Event.NEXT;
}


var LDTrial;
function LDTrialLoopBegin(LDTrialLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    LDTrial = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'LDWordList.xlsx',
      seed: undefined, name: 'LDTrial'
    });
    psychoJS.experiment.addLoop(LDTrial); // add the loop to the experiment
    currentLoop = LDTrial;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    LDTrial.forEach(function() {
      const snapshot = LDTrial.getSnapshot();
    
      LDTrialLoopScheduler.add(importConditions(snapshot));
      LDTrialLoopScheduler.add(LDTaskRoutineBegin(snapshot));
      LDTrialLoopScheduler.add(LDTaskRoutineEachFrame());
      LDTrialLoopScheduler.add(LDTaskRoutineEnd());
      LDTrialLoopScheduler.add(LDResponse_2RoutineBegin(snapshot));
      LDTrialLoopScheduler.add(LDResponse_2RoutineEachFrame());
      LDTrialLoopScheduler.add(LDResponse_2RoutineEnd());
      LDTrialLoopScheduler.add(endLoopIteration(LDTrialLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function LDTrialLoopEnd() {
  psychoJS.experiment.removeLoop(LDTrial);

  return Scheduler.Event.NEXT;
}


async function LDTaskOrderLoopEnd() {
  psychoJS.experiment.removeLoop(LDTaskOrder);

  return Scheduler.Event.NEXT;
}


var SDTaskOrder;
function SDTaskOrderLoopBegin(SDTaskOrderLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    SDTaskOrder = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nRepsTask2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'SDTaskOrder'
    });
    psychoJS.experiment.addLoop(SDTaskOrder); // add the loop to the experiment
    currentLoop = SDTaskOrder;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    SDTaskOrder.forEach(function() {
      const snapshot = SDTaskOrder.getSnapshot();
    
      SDTaskOrderLoopScheduler.add(importConditions(snapshot));
      SDTaskOrderLoopScheduler.add(SDInitalCodeRoutineBegin(snapshot));
      SDTaskOrderLoopScheduler.add(SDInitalCodeRoutineEachFrame());
      SDTaskOrderLoopScheduler.add(SDInitalCodeRoutineEnd());
      SDTaskOrderLoopScheduler.add(SDInst1RoutineBegin(snapshot));
      SDTaskOrderLoopScheduler.add(SDInst1RoutineEachFrame());
      SDTaskOrderLoopScheduler.add(SDInst1RoutineEnd());
      SDTaskOrderLoopScheduler.add(SDInst2RoutineBegin(snapshot));
      SDTaskOrderLoopScheduler.add(SDInst2RoutineEachFrame());
      SDTaskOrderLoopScheduler.add(SDInst2RoutineEnd());
      SDTaskOrderLoopScheduler.add(SDPracticeInstRoutineBegin(snapshot));
      SDTaskOrderLoopScheduler.add(SDPracticeInstRoutineEachFrame());
      SDTaskOrderLoopScheduler.add(SDPracticeInstRoutineEnd());
      SDTaskOrderLoopScheduler.add(fixationInst_4RoutineBegin(snapshot));
      SDTaskOrderLoopScheduler.add(fixationInst_4RoutineEachFrame());
      SDTaskOrderLoopScheduler.add(fixationInst_4RoutineEnd());
      const SDPracticeTrialLoopScheduler = new Scheduler(psychoJS);
      SDTaskOrderLoopScheduler.add(SDPracticeTrialLoopBegin(SDPracticeTrialLoopScheduler, snapshot));
      SDTaskOrderLoopScheduler.add(SDPracticeTrialLoopScheduler);
      SDTaskOrderLoopScheduler.add(SDPracticeTrialLoopEnd);
      SDTaskOrderLoopScheduler.add(SDTaskInstRoutineBegin(snapshot));
      SDTaskOrderLoopScheduler.add(SDTaskInstRoutineEachFrame());
      SDTaskOrderLoopScheduler.add(SDTaskInstRoutineEnd());
      const SDTRialLoopScheduler = new Scheduler(psychoJS);
      SDTaskOrderLoopScheduler.add(SDTRialLoopBegin(SDTRialLoopScheduler, snapshot));
      SDTaskOrderLoopScheduler.add(SDTRialLoopScheduler);
      SDTaskOrderLoopScheduler.add(SDTRialLoopEnd);
      SDTaskOrderLoopScheduler.add(SDBreakRoutineBegin(snapshot));
      SDTaskOrderLoopScheduler.add(SDBreakRoutineEachFrame());
      SDTaskOrderLoopScheduler.add(SDBreakRoutineEnd());
      SDTaskOrderLoopScheduler.add(endLoopIteration(SDTaskOrderLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var SDPracticeTrial;
function SDPracticeTrialLoopBegin(SDPracticeTrialLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    SDPracticeTrial = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'SD_PracticeArb.xlsx',
      seed: undefined, name: 'SDPracticeTrial'
    });
    psychoJS.experiment.addLoop(SDPracticeTrial); // add the loop to the experiment
    currentLoop = SDPracticeTrial;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    SDPracticeTrial.forEach(function() {
      const snapshot = SDPracticeTrial.getSnapshot();
    
      SDPracticeTrialLoopScheduler.add(importConditions(snapshot));
      SDPracticeTrialLoopScheduler.add(SDPracticeRoutineBegin(snapshot));
      SDPracticeTrialLoopScheduler.add(SDPracticeRoutineEachFrame());
      SDPracticeTrialLoopScheduler.add(SDPracticeRoutineEnd());
      SDPracticeTrialLoopScheduler.add(SDPracticeResponseRoutineBegin(snapshot));
      SDPracticeTrialLoopScheduler.add(SDPracticeResponseRoutineEachFrame());
      SDPracticeTrialLoopScheduler.add(SDPracticeResponseRoutineEnd());
      SDPracticeTrialLoopScheduler.add(endLoopIteration(SDPracticeTrialLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function SDPracticeTrialLoopEnd() {
  psychoJS.experiment.removeLoop(SDPracticeTrial);

  return Scheduler.Event.NEXT;
}


var SDTRial;
function SDTRialLoopBegin(SDTRialLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    SDTRial = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'SDWordList.xlsx',
      seed: undefined, name: 'SDTRial'
    });
    psychoJS.experiment.addLoop(SDTRial); // add the loop to the experiment
    currentLoop = SDTRial;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    SDTRial.forEach(function() {
      const snapshot = SDTRial.getSnapshot();
    
      SDTRialLoopScheduler.add(importConditions(snapshot));
      SDTRialLoopScheduler.add(SDTaskRoutineBegin(snapshot));
      SDTRialLoopScheduler.add(SDTaskRoutineEachFrame());
      SDTRialLoopScheduler.add(SDTaskRoutineEnd());
      SDTRialLoopScheduler.add(SDResponseRoutineBegin(snapshot));
      SDTRialLoopScheduler.add(SDResponseRoutineEachFrame());
      SDTRialLoopScheduler.add(SDResponseRoutineEnd());
      SDTRialLoopScheduler.add(endLoopIteration(SDTRialLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function SDTRialLoopEnd() {
  psychoJS.experiment.removeLoop(SDTRial);

  return Scheduler.Event.NEXT;
}


async function SDTaskOrderLoopEnd() {
  psychoJS.experiment.removeLoop(SDTaskOrder);

  return Scheduler.Event.NEXT;
}


async function taskOrderLoopEnd() {
  psychoJS.experiment.removeLoop(taskOrder);

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _CommonInstResp1_allKeys;
var taskOrderCodeComponents;
function taskOrderCodeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'taskOrderCode'-------
    t = 0;
    taskOrderCodeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    CommonInstResp1.keys = undefined;
    CommonInstResp1.rt = undefined;
    _CommonInstResp1_allKeys = [];
    // keep track of which components have finished
    taskOrderCodeComponents = [];
    taskOrderCodeComponents.push(CommonInst1);
    taskOrderCodeComponents.push(CommonInstResp1);
    
    taskOrderCodeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function taskOrderCodeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'taskOrderCode'-------
    // get current time
    t = taskOrderCodeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *CommonInst1* updates
    if (t >= 0.0 && CommonInst1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CommonInst1.tStart = t;  // (not accounting for frame time here)
      CommonInst1.frameNStart = frameN;  // exact frame index
      
      CommonInst1.setAutoDraw(true);
    }

    
    // *CommonInstResp1* updates
    if (t >= 0.0 && CommonInstResp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CommonInstResp1.tStart = t;  // (not accounting for frame time here)
      CommonInstResp1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { CommonInstResp1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { CommonInstResp1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { CommonInstResp1.clearEvents(); });
    }

    if (CommonInstResp1.status === PsychoJS.Status.STARTED) {
      let theseKeys = CommonInstResp1.getKeys({keyList: ['space', '0', '1'], waitRelease: false});
      _CommonInstResp1_allKeys = _CommonInstResp1_allKeys.concat(theseKeys);
      if (_CommonInstResp1_allKeys.length > 0) {
        CommonInstResp1.keys = _CommonInstResp1_allKeys[_CommonInstResp1_allKeys.length - 1].name;  // just the last key pressed
        CommonInstResp1.rt = _CommonInstResp1_allKeys[_CommonInstResp1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    taskOrderCodeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function taskOrderCodeRoutineEnd() {
  return async function () {
    //------Ending Routine 'taskOrderCode'-------
    taskOrderCodeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    CommonInstResp1.stop();
    // the Routine "taskOrderCode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var innitialCodeComponents;
function innitialCodeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'innitialCode'-------
    t = 0;
    innitialCodeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    innitialCodeComponents = [];
    
    innitialCodeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function innitialCodeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'innitialCode'-------
    // get current time
    t = innitialCodeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    innitialCodeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function innitialCodeRoutineEnd() {
  return async function () {
    //------Ending Routine 'innitialCode'-------
    innitialCodeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "innitialCode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _LDInst1Resp_allKeys;
var LDInst1Components;
function LDInst1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'LDInst1'-------
    t = 0;
    LDInst1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    LDInst1Resp.keys = undefined;
    LDInst1Resp.rt = undefined;
    _LDInst1Resp_allKeys = [];
    // keep track of which components have finished
    LDInst1Components = [];
    LDInst1Components.push(LDInst_1);
    LDInst1Components.push(LDInst1Resp);
    
    LDInst1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function LDInst1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'LDInst1'-------
    // get current time
    t = LDInst1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *LDInst_1* updates
    if (t >= 0.0 && LDInst_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LDInst_1.tStart = t;  // (not accounting for frame time here)
      LDInst_1.frameNStart = frameN;  // exact frame index
      
      LDInst_1.setAutoDraw(true);
    }

    
    // *LDInst1Resp* updates
    if (t >= 0.0 && LDInst1Resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LDInst1Resp.tStart = t;  // (not accounting for frame time here)
      LDInst1Resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { LDInst1Resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { LDInst1Resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { LDInst1Resp.clearEvents(); });
    }

    if (LDInst1Resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = LDInst1Resp.getKeys({keyList: ['space'], waitRelease: false});
      _LDInst1Resp_allKeys = _LDInst1Resp_allKeys.concat(theseKeys);
      if (_LDInst1Resp_allKeys.length > 0) {
        LDInst1Resp.keys = _LDInst1Resp_allKeys[_LDInst1Resp_allKeys.length - 1].name;  // just the last key pressed
        LDInst1Resp.rt = _LDInst1Resp_allKeys[_LDInst1Resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    LDInst1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LDInst1RoutineEnd() {
  return async function () {
    //------Ending Routine 'LDInst1'-------
    LDInst1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    LDInst1Resp.stop();
    // the Routine "LDInst1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _LDInst2Resp_allKeys;
var LDInst2Components;
function LDInst2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'LDInst2'-------
    t = 0;
    LDInst2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    LDInst2Resp.keys = undefined;
    LDInst2Resp.rt = undefined;
    _LDInst2Resp_allKeys = [];
    // keep track of which components have finished
    LDInst2Components = [];
    LDInst2Components.push(LDInst_2);
    LDInst2Components.push(LDInst2Resp);
    
    LDInst2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function LDInst2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'LDInst2'-------
    // get current time
    t = LDInst2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *LDInst_2* updates
    if (t >= 0.0 && LDInst_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LDInst_2.tStart = t;  // (not accounting for frame time here)
      LDInst_2.frameNStart = frameN;  // exact frame index
      
      LDInst_2.setAutoDraw(true);
    }

    
    // *LDInst2Resp* updates
    if (t >= 0.0 && LDInst2Resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LDInst2Resp.tStart = t;  // (not accounting for frame time here)
      LDInst2Resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { LDInst2Resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { LDInst2Resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { LDInst2Resp.clearEvents(); });
    }

    if (LDInst2Resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = LDInst2Resp.getKeys({keyList: ['space'], waitRelease: false});
      _LDInst2Resp_allKeys = _LDInst2Resp_allKeys.concat(theseKeys);
      if (_LDInst2Resp_allKeys.length > 0) {
        LDInst2Resp.keys = _LDInst2Resp_allKeys[_LDInst2Resp_allKeys.length - 1].name;  // just the last key pressed
        LDInst2Resp.rt = _LDInst2Resp_allKeys[_LDInst2Resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    LDInst2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LDInst2RoutineEnd() {
  return async function () {
    //------Ending Routine 'LDInst2'-------
    LDInst2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    LDInst2Resp.stop();
    // the Routine "LDInst2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _practiceInstResp_allKeys;
var LDPracticeInstComponents;
function LDPracticeInstRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'LDPracticeInst'-------
    t = 0;
    LDPracticeInstClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    practiceInstResp.keys = undefined;
    practiceInstResp.rt = undefined;
    _practiceInstResp_allKeys = [];
    // keep track of which components have finished
    LDPracticeInstComponents = [];
    LDPracticeInstComponents.push(practiceInst);
    LDPracticeInstComponents.push(practiceInstResp);
    
    LDPracticeInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function LDPracticeInstRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'LDPracticeInst'-------
    // get current time
    t = LDPracticeInstClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practiceInst* updates
    if (t >= 0.0 && practiceInst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceInst.tStart = t;  // (not accounting for frame time here)
      practiceInst.frameNStart = frameN;  // exact frame index
      
      practiceInst.setAutoDraw(true);
    }

    
    // *practiceInstResp* updates
    if (t >= 0.0 && practiceInstResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practiceInstResp.tStart = t;  // (not accounting for frame time here)
      practiceInstResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { practiceInstResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { practiceInstResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { practiceInstResp.clearEvents(); });
    }

    if (practiceInstResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = practiceInstResp.getKeys({keyList: ['space'], waitRelease: false});
      _practiceInstResp_allKeys = _practiceInstResp_allKeys.concat(theseKeys);
      if (_practiceInstResp_allKeys.length > 0) {
        practiceInstResp.keys = _practiceInstResp_allKeys[_practiceInstResp_allKeys.length - 1].name;  // just the last key pressed
        practiceInstResp.rt = _practiceInstResp_allKeys[_practiceInstResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    LDPracticeInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LDPracticeInstRoutineEnd() {
  return async function () {
    //------Ending Routine 'LDPracticeInst'-------
    LDPracticeInstComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    practiceInstResp.stop();
    // the Routine "LDPracticeInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _fixationInstResp_allKeys;
var fixationInstComponents;
function fixationInstRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'fixationInst'-------
    t = 0;
    fixationInstClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    fixationInstResp.keys = undefined;
    fixationInstResp.rt = undefined;
    _fixationInstResp_allKeys = [];
    // keep track of which components have finished
    fixationInstComponents = [];
    fixationInstComponents.push(fixationInst_1);
    fixationInstComponents.push(fixationInstResp);
    
    fixationInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function fixationInstRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'fixationInst'-------
    // get current time
    t = fixationInstClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixationInst_1* updates
    if (t >= 0.0 && fixationInst_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationInst_1.tStart = t;  // (not accounting for frame time here)
      fixationInst_1.frameNStart = frameN;  // exact frame index
      
      fixationInst_1.setAutoDraw(true);
    }

    
    // *fixationInstResp* updates
    if (t >= 0.0 && fixationInstResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationInstResp.tStart = t;  // (not accounting for frame time here)
      fixationInstResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { fixationInstResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { fixationInstResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { fixationInstResp.clearEvents(); });
    }

    if (fixationInstResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = fixationInstResp.getKeys({keyList: ['space'], waitRelease: false});
      _fixationInstResp_allKeys = _fixationInstResp_allKeys.concat(theseKeys);
      if (_fixationInstResp_allKeys.length > 0) {
        fixationInstResp.keys = _fixationInstResp_allKeys[_fixationInstResp_allKeys.length - 1].name;  // just the last key pressed
        fixationInstResp.rt = _fixationInstResp_allKeys[_fixationInstResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixationInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationInstRoutineEnd() {
  return async function () {
    //------Ending Routine 'fixationInst'-------
    fixationInstComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    fixationInstResp.stop();
    // the Routine "fixationInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var D_int;
var distractor;
var _PracticeResponse_allKeys;
var LDPracticeComponents;
function LDPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'LDPractice'-------
    t = 0;
    LDPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    D_int = util.randint(0, 84);
    xstim1_D = (- xword1);
    ystim1_D = (- yword1);
    stim1_D = list_Dist[Number.parseInt(D_int)];
    if ((D_int < 48)) {
        distractor = "word";
    } else {
        if ((D_int > 66)) {
            distractor = "consonants";
        } else {
            distractor = "pseudoword";
        }
    }
    
    noiseImage.setPos([xword1, yword1]);
    noiseImage_D.setPos([xstim1_D, ystim1_D]);
    wordPractice.setPos([xword1, yword1]);
    wordPractice.setText(word1);
    distWord.setPos([xstim1_D, ystim1_D]);
    distWord.setText(stim1_D);
    cue.setPos([xword1, (- 0.11)]);
    PracticeResponse.keys = undefined;
    PracticeResponse.rt = undefined;
    _PracticeResponse_allKeys = [];
    // keep track of which components have finished
    LDPracticeComponents = [];
    LDPracticeComponents.push(fixation);
    LDPracticeComponents.push(noiseImage);
    LDPracticeComponents.push(noiseImage_D);
    LDPracticeComponents.push(wordPractice);
    LDPracticeComponents.push(distWord);
    LDPracticeComponents.push(cue);
    LDPracticeComponents.push(PracticeResponse);
    
    LDPracticeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function LDPracticeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'LDPractice'-------
    // get current time
    t = LDPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation* updates
    if (t >= 0.2 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }

    
    // *noiseImage* updates
    if (t >= 0.4 && noiseImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noiseImage.tStart = t;  // (not accounting for frame time here)
      noiseImage.frameNStart = frameN;  // exact frame index
      
      noiseImage.setAutoDraw(true);
    }

    frameRemains = 0.4 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (noiseImage.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      noiseImage.setAutoDraw(false);
    }
    
    // *noiseImage_D* updates
    if (t >= 0.4 && noiseImage_D.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noiseImage_D.tStart = t;  // (not accounting for frame time here)
      noiseImage_D.frameNStart = frameN;  // exact frame index
      
      noiseImage_D.setAutoDraw(true);
    }

    frameRemains = 0.4 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (noiseImage_D.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      noiseImage_D.setAutoDraw(false);
    }
    
    // *wordPractice* updates
    if (t >= 0.6 && wordPractice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wordPractice.tStart = t;  // (not accounting for frame time here)
      wordPractice.frameNStart = frameN;  // exact frame index
      
      wordPractice.setAutoDraw(true);
    }

    frameRemains = 0.6 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (wordPractice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wordPractice.setAutoDraw(false);
    }
    
    // *distWord* updates
    if (t >= 0.6 && distWord.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      distWord.tStart = t;  // (not accounting for frame time here)
      distWord.frameNStart = frameN;  // exact frame index
      
      distWord.setAutoDraw(true);
    }

    frameRemains = 0.6 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (distWord.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      distWord.setAutoDraw(false);
    }
    
    // *cue* updates
    if (t >= 0.6 && cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cue.tStart = t;  // (not accounting for frame time here)
      cue.frameNStart = frameN;  // exact frame index
      
      cue.setAutoDraw(true);
    }

    frameRemains = 0.6 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cue.setAutoDraw(false);
    }
    
    // *PracticeResponse* updates
    if (t >= 0.6 && PracticeResponse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeResponse.tStart = t;  // (not accounting for frame time here)
      PracticeResponse.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PracticeResponse.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PracticeResponse.start(); }); // start on screen flip
    }

    if (PracticeResponse.status === PsychoJS.Status.STARTED) {
      let theseKeys = PracticeResponse.getKeys({keyList: ['1', '2', 'esc'], waitRelease: false});
      _PracticeResponse_allKeys = _PracticeResponse_allKeys.concat(theseKeys);
      if (_PracticeResponse_allKeys.length > 0) {
        PracticeResponse.keys = _PracticeResponse_allKeys[_PracticeResponse_allKeys.length - 1].name;  // just the last key pressed
        PracticeResponse.rt = _PracticeResponse_allKeys[_PracticeResponse_allKeys.length - 1].rt;
        // was this correct?
        if (PracticeResponse.keys == corrAns) {
            PracticeResponse.corr = 1;
        } else {
            PracticeResponse.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    LDPracticeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LDPracticeRoutineEnd() {
  return async function () {
    //------Ending Routine 'LDPractice'-------
    LDPracticeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    practiceTrial.addData("distractor", distractor);
    
    // was no response the correct answer?!
    if (PracticeResponse.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         PracticeResponse.corr = 1;  // correct non-response
      } else {
         PracticeResponse.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('PracticeResponse.keys', PracticeResponse.keys);
    psychoJS.experiment.addData('PracticeResponse.corr', PracticeResponse.corr);
    if (typeof PracticeResponse.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('PracticeResponse.rt', PracticeResponse.rt);
        routineTimer.reset();
        }
    
    PracticeResponse.stop();
    // the Routine "LDPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var feedbackPitch;
var LDPRacticeResponseComponents;
function LDPRacticeResponseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'LDPRacticeResponse'-------
    t = 0;
    LDPRacticeResponseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.030000);
    // update component parameters for each repeat
    if (PracticeResponse.corr) {
        feedbackPitch = soundfile[0];
    } else {
        feedbackPitch = soundfile[1];
    }
    
    feedback = new sound.Sound({
    win: psychoJS.window,
    value: feedbackPitch,
    secs: 0.03,
    });
    feedback.secs=0.03;
    feedback.setVolume(1.0);
    // keep track of which components have finished
    LDPRacticeResponseComponents = [];
    LDPRacticeResponseComponents.push(feedback);
    
    LDPRacticeResponseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function LDPRacticeResponseRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'LDPRacticeResponse'-------
    // get current time
    t = LDPRacticeResponseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop feedback
    if (t >= 0.0 && feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback.tStart = t;  // (not accounting for frame time here)
      feedback.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ feedback.play(); });  // screen flip
      feedback.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.03 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.03 > 0.5) {  feedback.stop();  // stop the sound (if longer than duration)
        feedback.status = PsychoJS.Status.FINISHED;
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    LDPRacticeResponseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LDPRacticeResponseRoutineEnd() {
  return async function () {
    //------Ending Routine 'LDPRacticeResponse'-------
    LDPRacticeResponseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    feedback.stop();  // ensure sound has stopped at end of routine
    return Scheduler.Event.NEXT;
  };
}


var _LDTaskResp_allKeys;
var taskInstComponents;
function taskInstRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'taskInst'-------
    t = 0;
    taskInstClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    LDInstructrions.setAlignHoriz("left");
    LDInstructionArb.setAlignHoriz("right");
    
    LDTaskResp.keys = undefined;
    LDTaskResp.rt = undefined;
    _LDTaskResp_allKeys = [];
    // keep track of which components have finished
    taskInstComponents = [];
    taskInstComponents.push(LDTaskResp);
    taskInstComponents.push(LDInstructrions);
    taskInstComponents.push(LDInstructionArb);
    
    taskInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function taskInstRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'taskInst'-------
    // get current time
    t = taskInstClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *LDTaskResp* updates
    if (t >= 0.0 && LDTaskResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LDTaskResp.tStart = t;  // (not accounting for frame time here)
      LDTaskResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { LDTaskResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { LDTaskResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { LDTaskResp.clearEvents(); });
    }

    if (LDTaskResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = LDTaskResp.getKeys({keyList: ['space'], waitRelease: false});
      _LDTaskResp_allKeys = _LDTaskResp_allKeys.concat(theseKeys);
      if (_LDTaskResp_allKeys.length > 0) {
        LDTaskResp.keys = _LDTaskResp_allKeys[_LDTaskResp_allKeys.length - 1].name;  // just the last key pressed
        LDTaskResp.rt = _LDTaskResp_allKeys[_LDTaskResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *LDInstructrions* updates
    if (t >= 0.0 && LDInstructrions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LDInstructrions.tStart = t;  // (not accounting for frame time here)
      LDInstructrions.frameNStart = frameN;  // exact frame index
      
      LDInstructrions.setAutoDraw(true);
    }

    
    // *LDInstructionArb* updates
    if (t >= 0.0 && LDInstructionArb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LDInstructionArb.tStart = t;  // (not accounting for frame time here)
      LDInstructionArb.frameNStart = frameN;  // exact frame index
      
      LDInstructionArb.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    taskInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function taskInstRoutineEnd() {
  return async function () {
    //------Ending Routine 'taskInst'-------
    taskInstComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    LDTaskResp.stop();
    // the Routine "taskInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _LDResponse_allKeys;
var LDTaskComponents;
function LDTaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'LDTask'-------
    t = 0;
    LDTaskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    /* Syntax Error: Fix Python code */
    noiseImage_2.setPos([xword1, yword1]);
    noiseImage_D_2.setPos([xstim1_D, ystim1_D]);
    LDWord_1.setPos([xword1, yword1]);
    LDWord_1.setText(word1);
    distWord_2.setPos([xword1_D, yword1_D]);
    distWord_2.setText(word1_D);
    cue_2.setPos([xword1, (- 0.11)]);
    LDResponse.keys = undefined;
    LDResponse.rt = undefined;
    _LDResponse_allKeys = [];
    // keep track of which components have finished
    LDTaskComponents = [];
    LDTaskComponents.push(fixation_2);
    LDTaskComponents.push(noiseImage_2);
    LDTaskComponents.push(noiseImage_D_2);
    LDTaskComponents.push(LDWord_1);
    LDTaskComponents.push(distWord_2);
    LDTaskComponents.push(cue_2);
    LDTaskComponents.push(LDResponse);
    
    LDTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function LDTaskRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'LDTask'-------
    // get current time
    t = LDTaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_2* updates
    if (t >= 0.2 && fixation_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_2.tStart = t;  // (not accounting for frame time here)
      fixation_2.frameNStart = frameN;  // exact frame index
      
      fixation_2.setAutoDraw(true);
    }

    
    // *noiseImage_2* updates
    if (t >= 0.4 && noiseImage_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noiseImage_2.tStart = t;  // (not accounting for frame time here)
      noiseImage_2.frameNStart = frameN;  // exact frame index
      
      noiseImage_2.setAutoDraw(true);
    }

    frameRemains = 0.4 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (noiseImage_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      noiseImage_2.setAutoDraw(false);
    }
    
    // *noiseImage_D_2* updates
    if (t >= 0.4 && noiseImage_D_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noiseImage_D_2.tStart = t;  // (not accounting for frame time here)
      noiseImage_D_2.frameNStart = frameN;  // exact frame index
      
      noiseImage_D_2.setAutoDraw(true);
    }

    frameRemains = 0.4 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (noiseImage_D_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      noiseImage_D_2.setAutoDraw(false);
    }
    
    // *LDWord_1* updates
    if (t >= 0.6 && LDWord_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LDWord_1.tStart = t;  // (not accounting for frame time here)
      LDWord_1.frameNStart = frameN;  // exact frame index
      
      LDWord_1.setAutoDraw(true);
    }

    frameRemains = 0.6 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (LDWord_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      LDWord_1.setAutoDraw(false);
    }
    
    // *distWord_2* updates
    if (t >= 0.6 && distWord_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      distWord_2.tStart = t;  // (not accounting for frame time here)
      distWord_2.frameNStart = frameN;  // exact frame index
      
      distWord_2.setAutoDraw(true);
    }

    frameRemains = 0.6 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (distWord_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      distWord_2.setAutoDraw(false);
    }
    
    // *cue_2* updates
    if (t >= 0.6 && cue_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cue_2.tStart = t;  // (not accounting for frame time here)
      cue_2.frameNStart = frameN;  // exact frame index
      
      cue_2.setAutoDraw(true);
    }

    frameRemains = 0.6 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cue_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cue_2.setAutoDraw(false);
    }
    
    // *LDResponse* updates
    if (t >= 0.6 && LDResponse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LDResponse.tStart = t;  // (not accounting for frame time here)
      LDResponse.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { LDResponse.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { LDResponse.start(); }); // start on screen flip
    }

    if (LDResponse.status === PsychoJS.Status.STARTED) {
      let theseKeys = LDResponse.getKeys({keyList: ['1', '2', 'esc'], waitRelease: false});
      _LDResponse_allKeys = _LDResponse_allKeys.concat(theseKeys);
      if (_LDResponse_allKeys.length > 0) {
        LDResponse.keys = _LDResponse_allKeys[_LDResponse_allKeys.length - 1].name;  // just the last key pressed
        LDResponse.rt = _LDResponse_allKeys[_LDResponse_allKeys.length - 1].rt;
        // was this correct?
        if (LDResponse.keys == corrAns) {
            LDResponse.corr = 1;
        } else {
            LDResponse.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    LDTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LDTaskRoutineEnd() {
  return async function () {
    //------Ending Routine 'LDTask'-------
    LDTaskComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    /* Syntax Error: Fix Python code */
    // was no response the correct answer?!
    if (LDResponse.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         LDResponse.corr = 1;  // correct non-response
      } else {
         LDResponse.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('LDResponse.keys', LDResponse.keys);
    psychoJS.experiment.addData('LDResponse.corr', LDResponse.corr);
    if (typeof LDResponse.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('LDResponse.rt', LDResponse.rt);
        routineTimer.reset();
        }
    
    LDResponse.stop();
    // the Routine "LDTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var LDResponse_2Components;
function LDResponse_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'LDResponse_2'-------
    t = 0;
    LDResponse_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.030000);
    // update component parameters for each repeat
    if (LDResponse.corr) {
        feedbackPitch = soundfile[0];
    } else {
        feedbackPitch = soundfile[1];
    }
    
    feedback_2 = new sound.Sound({
    win: psychoJS.window,
    value: feedbackPitch,
    secs: 0.03,
    });
    feedback_2.secs=0.03;
    feedback_2.setVolume(1.0);
    // keep track of which components have finished
    LDResponse_2Components = [];
    LDResponse_2Components.push(feedback_2);
    
    LDResponse_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function LDResponse_2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'LDResponse_2'-------
    // get current time
    t = LDResponse_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop feedback_2
    if (t >= 0.0 && feedback_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_2.tStart = t;  // (not accounting for frame time here)
      feedback_2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ feedback_2.play(); });  // screen flip
      feedback_2.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.03 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.03 > 0.5) {  feedback_2.stop();  // stop the sound (if longer than duration)
        feedback_2.status = PsychoJS.Status.FINISHED;
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    LDResponse_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LDResponse_2RoutineEnd() {
  return async function () {
    //------Ending Routine 'LDResponse_2'-------
    LDResponse_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    feedback_2.stop();  // ensure sound has stopped at end of routine
    return Scheduler.Event.NEXT;
  };
}


var _LDBreakResp_allKeys;
var LDBreakComponents;
function LDBreakRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'LDBreak'-------
    t = 0;
    LDBreakClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    endOfLD.setAlignHoriz("left");
    endOfLDArb.setAlignHoriz("right");
    
    LDBreakResp.keys = undefined;
    LDBreakResp.rt = undefined;
    _LDBreakResp_allKeys = [];
    // keep track of which components have finished
    LDBreakComponents = [];
    LDBreakComponents.push(LDBreakResp);
    LDBreakComponents.push(endOfLD);
    LDBreakComponents.push(endOfLDArb);
    
    LDBreakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function LDBreakRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'LDBreak'-------
    // get current time
    t = LDBreakClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *LDBreakResp* updates
    if (t >= 0.0 && LDBreakResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LDBreakResp.tStart = t;  // (not accounting for frame time here)
      LDBreakResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { LDBreakResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { LDBreakResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { LDBreakResp.clearEvents(); });
    }

    if (LDBreakResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = LDBreakResp.getKeys({keyList: ['space'], waitRelease: false});
      _LDBreakResp_allKeys = _LDBreakResp_allKeys.concat(theseKeys);
      if (_LDBreakResp_allKeys.length > 0) {
        LDBreakResp.keys = _LDBreakResp_allKeys[_LDBreakResp_allKeys.length - 1].name;  // just the last key pressed
        LDBreakResp.rt = _LDBreakResp_allKeys[_LDBreakResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *endOfLD* updates
    if (t >= 0.0 && endOfLD.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endOfLD.tStart = t;  // (not accounting for frame time here)
      endOfLD.frameNStart = frameN;  // exact frame index
      
      endOfLD.setAutoDraw(true);
    }

    
    // *endOfLDArb* updates
    if (t >= 0.0 && endOfLDArb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endOfLDArb.tStart = t;  // (not accounting for frame time here)
      endOfLDArb.frameNStart = frameN;  // exact frame index
      
      endOfLDArb.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    LDBreakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LDBreakRoutineEnd() {
  return async function () {
    //------Ending Routine 'LDBreak'-------
    LDBreakComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('LDBreakResp.keys', LDBreakResp.keys);
    if (typeof LDBreakResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('LDBreakResp.rt', LDBreakResp.rt);
        routineTimer.reset();
        }
    
    LDBreakResp.stop();
    // the Routine "LDBreak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var SDInitalCodeComponents;
function SDInitalCodeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'SDInitalCode'-------
    t = 0;
    SDInitalCodeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    SDInitalCodeComponents = [];
    
    SDInitalCodeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SDInitalCodeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'SDInitalCode'-------
    // get current time
    t = SDInitalCodeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SDInitalCodeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SDInitalCodeRoutineEnd() {
  return async function () {
    //------Ending Routine 'SDInitalCode'-------
    SDInitalCodeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "SDInitalCode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _SDInst1Resp_allKeys;
var SDInst1Components;
function SDInst1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'SDInst1'-------
    t = 0;
    SDInst1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    SDInst1Resp.keys = undefined;
    SDInst1Resp.rt = undefined;
    _SDInst1Resp_allKeys = [];
    // keep track of which components have finished
    SDInst1Components = [];
    SDInst1Components.push(SDInst_1);
    SDInst1Components.push(SDInst1Resp);
    
    SDInst1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SDInst1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'SDInst1'-------
    // get current time
    t = SDInst1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SDInst_1* updates
    if (t >= 0.0 && SDInst_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDInst_1.tStart = t;  // (not accounting for frame time here)
      SDInst_1.frameNStart = frameN;  // exact frame index
      
      SDInst_1.setAutoDraw(true);
    }

    
    // *SDInst1Resp* updates
    if (t >= 0.0 && SDInst1Resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDInst1Resp.tStart = t;  // (not accounting for frame time here)
      SDInst1Resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SDInst1Resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SDInst1Resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { SDInst1Resp.clearEvents(); });
    }

    if (SDInst1Resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = SDInst1Resp.getKeys({keyList: ['space'], waitRelease: false});
      _SDInst1Resp_allKeys = _SDInst1Resp_allKeys.concat(theseKeys);
      if (_SDInst1Resp_allKeys.length > 0) {
        SDInst1Resp.keys = _SDInst1Resp_allKeys[_SDInst1Resp_allKeys.length - 1].name;  // just the last key pressed
        SDInst1Resp.rt = _SDInst1Resp_allKeys[_SDInst1Resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SDInst1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SDInst1RoutineEnd() {
  return async function () {
    //------Ending Routine 'SDInst1'-------
    SDInst1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    SDInst1Resp.stop();
    // the Routine "SDInst1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _SDInst2Resp_allKeys;
var SDInst2Components;
function SDInst2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'SDInst2'-------
    t = 0;
    SDInst2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    SDInst2Resp.keys = undefined;
    SDInst2Resp.rt = undefined;
    _SDInst2Resp_allKeys = [];
    // keep track of which components have finished
    SDInst2Components = [];
    SDInst2Components.push(SDInst_2);
    SDInst2Components.push(SDInst2Resp);
    
    SDInst2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SDInst2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'SDInst2'-------
    // get current time
    t = SDInst2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SDInst_2* updates
    if (t >= 0.0 && SDInst_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDInst_2.tStart = t;  // (not accounting for frame time here)
      SDInst_2.frameNStart = frameN;  // exact frame index
      
      SDInst_2.setAutoDraw(true);
    }

    
    // *SDInst2Resp* updates
    if (t >= 0.0 && SDInst2Resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDInst2Resp.tStart = t;  // (not accounting for frame time here)
      SDInst2Resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SDInst2Resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SDInst2Resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { SDInst2Resp.clearEvents(); });
    }

    if (SDInst2Resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = SDInst2Resp.getKeys({keyList: ['space'], waitRelease: false});
      _SDInst2Resp_allKeys = _SDInst2Resp_allKeys.concat(theseKeys);
      if (_SDInst2Resp_allKeys.length > 0) {
        SDInst2Resp.keys = _SDInst2Resp_allKeys[_SDInst2Resp_allKeys.length - 1].name;  // just the last key pressed
        SDInst2Resp.rt = _SDInst2Resp_allKeys[_SDInst2Resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SDInst2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SDInst2RoutineEnd() {
  return async function () {
    //------Ending Routine 'SDInst2'-------
    SDInst2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    SDInst2Resp.stop();
    // the Routine "SDInst2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _SDPracticeInstResp_allKeys;
var SDPracticeInstComponents;
function SDPracticeInstRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'SDPracticeInst'-------
    t = 0;
    SDPracticeInstClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    SDPracticeInstResp.keys = undefined;
    SDPracticeInstResp.rt = undefined;
    _SDPracticeInstResp_allKeys = [];
    // keep track of which components have finished
    SDPracticeInstComponents = [];
    SDPracticeInstComponents.push(SDPractiveInst_1);
    SDPracticeInstComponents.push(SDPracticeInstResp);
    
    SDPracticeInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SDPracticeInstRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'SDPracticeInst'-------
    // get current time
    t = SDPracticeInstClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SDPractiveInst_1* updates
    if (t >= 0.0 && SDPractiveInst_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDPractiveInst_1.tStart = t;  // (not accounting for frame time here)
      SDPractiveInst_1.frameNStart = frameN;  // exact frame index
      
      SDPractiveInst_1.setAutoDraw(true);
    }

    
    // *SDPracticeInstResp* updates
    if (t >= 0.0 && SDPracticeInstResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDPracticeInstResp.tStart = t;  // (not accounting for frame time here)
      SDPracticeInstResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SDPracticeInstResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SDPracticeInstResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { SDPracticeInstResp.clearEvents(); });
    }

    if (SDPracticeInstResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = SDPracticeInstResp.getKeys({keyList: ['space'], waitRelease: false});
      _SDPracticeInstResp_allKeys = _SDPracticeInstResp_allKeys.concat(theseKeys);
      if (_SDPracticeInstResp_allKeys.length > 0) {
        SDPracticeInstResp.keys = _SDPracticeInstResp_allKeys[_SDPracticeInstResp_allKeys.length - 1].name;  // just the last key pressed
        SDPracticeInstResp.rt = _SDPracticeInstResp_allKeys[_SDPracticeInstResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SDPracticeInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SDPracticeInstRoutineEnd() {
  return async function () {
    //------Ending Routine 'SDPracticeInst'-------
    SDPracticeInstComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    SDPracticeInstResp.stop();
    // the Routine "SDPracticeInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _fixationInst4Resp_allKeys;
var fixationInst_4Components;
function fixationInst_4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'fixationInst_4'-------
    t = 0;
    fixationInst_4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    fixationInst4Resp.keys = undefined;
    fixationInst4Resp.rt = undefined;
    _fixationInst4Resp_allKeys = [];
    // keep track of which components have finished
    fixationInst_4Components = [];
    fixationInst_4Components.push(fixationInst_5);
    fixationInst_4Components.push(fixationInst4Resp);
    
    fixationInst_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function fixationInst_4RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'fixationInst_4'-------
    // get current time
    t = fixationInst_4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixationInst_5* updates
    if (t >= 0.0 && fixationInst_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationInst_5.tStart = t;  // (not accounting for frame time here)
      fixationInst_5.frameNStart = frameN;  // exact frame index
      
      fixationInst_5.setAutoDraw(true);
    }

    
    // *fixationInst4Resp* updates
    if (t >= 0.0 && fixationInst4Resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationInst4Resp.tStart = t;  // (not accounting for frame time here)
      fixationInst4Resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { fixationInst4Resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { fixationInst4Resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { fixationInst4Resp.clearEvents(); });
    }

    if (fixationInst4Resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = fixationInst4Resp.getKeys({keyList: ['space'], waitRelease: false});
      _fixationInst4Resp_allKeys = _fixationInst4Resp_allKeys.concat(theseKeys);
      if (_fixationInst4Resp_allKeys.length > 0) {
        fixationInst4Resp.keys = _fixationInst4Resp_allKeys[_fixationInst4Resp_allKeys.length - 1].name;  // just the last key pressed
        fixationInst4Resp.rt = _fixationInst4Resp_allKeys[_fixationInst4Resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixationInst_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationInst_4RoutineEnd() {
  return async function () {
    //------Ending Routine 'fixationInst_4'-------
    fixationInst_4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    fixationInst4Resp.stop();
    // the Routine "fixationInst_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var g;
var ystim2_D;
var _SDPracticeResp_allKeys;
var SDPracticeComponents;
function SDPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'SDPractice'-------
    t = 0;
    SDPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    g = util.randint(0, 2);
    D_int = util.randint(0, SDlist_limit);
    if ((g === 1)) {
        stim1 = word1;
        stim2 = word2;
        xstim1 = xword1;
        ystim1 = yword1;
        xstim2 = xword2;
        ystim2 = yword2;
        xstim1_D = (- xstim1);
        ystim1_D = (- ystim1);
        xstim2_D = (- xstim2);
        ystim2_D = (- ystim2);
        stim1_D = SDword1_Dist[Number.parseInt(D_int)];
        stim2_D = SDword2_Dist[Number.parseInt(D_int)];
    } else {
        stim1 = word2;
        stim2 = word1;
        xstim1 = xword2;
        ystim1 = yword2;
        xstim2 = xword1;
        ystim2 = yword1;
        xstim1_D = (- xstim1);
        ystim1_D = (- ystim1);
        xstim2_D = (- xstim2);
        ystim2_D = (- ystim2);
        stim1_D = SDword1_Dist[Number.parseInt(D_int)];
        stim2_D = SDword2_Dist[Number.parseInt(D_int)];
    }
    distractor = "word";
    
    SDPracticeWord1.setPos([xstim1, ystim1]);
    SDPracticeWord1.setText(stim1);
    SDPracticeDist1.setPos([xstim1_D, ystim1_D]);
    SDPracticeDist1.setText(stim1_D);
    cue_3.setPos([xstim1, (- 0.11)]);
    noiseImage_3.setPos([xstim1, ystim1]);
    noiseImage_D_3.setPos([xstim1_D, ystim1_D]);
    SDPracticeWord2.setPos([xstim2, ystim2]);
    SDPracticeWord2.setText(stim2);
    SDPracticeDist2.setPos([xstim2_D, ystim2_D]);
    SDPracticeDist2.setText(stim2_D);
    cue_6.setPos([xstim2, (- 0.11)]);
    SDPracticeResp.keys = undefined;
    SDPracticeResp.rt = undefined;
    _SDPracticeResp_allKeys = [];
    // keep track of which components have finished
    SDPracticeComponents = [];
    SDPracticeComponents.push(SDFixation);
    SDPracticeComponents.push(SDPracticeWord1);
    SDPracticeComponents.push(SDPracticeDist1);
    SDPracticeComponents.push(cue_3);
    SDPracticeComponents.push(noiseImage_3);
    SDPracticeComponents.push(noiseImage_D_3);
    SDPracticeComponents.push(SDPracticeWord2);
    SDPracticeComponents.push(SDPracticeDist2);
    SDPracticeComponents.push(cue_6);
    SDPracticeComponents.push(SDPracticeResp);
    
    SDPracticeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SDPracticeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'SDPractice'-------
    // get current time
    t = SDPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    SDPracticeTrial.addData("distractor", distractor);
    
    
    // *SDFixation* updates
    if (t >= 0.3 && SDFixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDFixation.tStart = t;  // (not accounting for frame time here)
      SDFixation.frameNStart = frameN;  // exact frame index
      
      SDFixation.setAutoDraw(true);
    }

    
    // *SDPracticeWord1* updates
    if (t >= 0.6 && SDPracticeWord1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDPracticeWord1.tStart = t;  // (not accounting for frame time here)
      SDPracticeWord1.frameNStart = frameN;  // exact frame index
      
      SDPracticeWord1.setAutoDraw(true);
    }

    frameRemains = 0.6 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (SDPracticeWord1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      SDPracticeWord1.setAutoDraw(false);
    }
    
    // *SDPracticeDist1* updates
    if (t >= 0.6 && SDPracticeDist1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDPracticeDist1.tStart = t;  // (not accounting for frame time here)
      SDPracticeDist1.frameNStart = frameN;  // exact frame index
      
      SDPracticeDist1.setAutoDraw(true);
    }

    frameRemains = 0.6 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (SDPracticeDist1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      SDPracticeDist1.setAutoDraw(false);
    }
    
    // *cue_3* updates
    if (t >= 0.6 && cue_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cue_3.tStart = t;  // (not accounting for frame time here)
      cue_3.frameNStart = frameN;  // exact frame index
      
      cue_3.setAutoDraw(true);
    }

    frameRemains = 0.6 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cue_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cue_3.setAutoDraw(false);
    }
    
    // *noiseImage_3* updates
    if (t >= 0.8 && noiseImage_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noiseImage_3.tStart = t;  // (not accounting for frame time here)
      noiseImage_3.frameNStart = frameN;  // exact frame index
      
      noiseImage_3.setAutoDraw(true);
    }

    frameRemains = 0.8 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (noiseImage_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      noiseImage_3.setAutoDraw(false);
    }
    
    // *noiseImage_D_3* updates
    if (t >= 0.8 && noiseImage_D_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noiseImage_D_3.tStart = t;  // (not accounting for frame time here)
      noiseImage_D_3.frameNStart = frameN;  // exact frame index
      
      noiseImage_D_3.setAutoDraw(true);
    }

    frameRemains = 0.8 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (noiseImage_D_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      noiseImage_D_3.setAutoDraw(false);
    }
    
    // *SDPracticeWord2* updates
    if (t >= 1.0 && SDPracticeWord2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDPracticeWord2.tStart = t;  // (not accounting for frame time here)
      SDPracticeWord2.frameNStart = frameN;  // exact frame index
      
      SDPracticeWord2.setAutoDraw(true);
    }

    frameRemains = 1.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (SDPracticeWord2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      SDPracticeWord2.setAutoDraw(false);
    }
    
    // *SDPracticeDist2* updates
    if (t >= 1.0 && SDPracticeDist2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDPracticeDist2.tStart = t;  // (not accounting for frame time here)
      SDPracticeDist2.frameNStart = frameN;  // exact frame index
      
      SDPracticeDist2.setAutoDraw(true);
    }

    frameRemains = 1.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (SDPracticeDist2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      SDPracticeDist2.setAutoDraw(false);
    }
    
    // *cue_6* updates
    if (t >= 1.0 && cue_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cue_6.tStart = t;  // (not accounting for frame time here)
      cue_6.frameNStart = frameN;  // exact frame index
      
      cue_6.setAutoDraw(true);
    }

    frameRemains = 1.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cue_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cue_6.setAutoDraw(false);
    }
    
    // *SDPracticeResp* updates
    if (t >= 1.0 && SDPracticeResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDPracticeResp.tStart = t;  // (not accounting for frame time here)
      SDPracticeResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SDPracticeResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SDPracticeResp.start(); }); // start on screen flip
    }

    if (SDPracticeResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = SDPracticeResp.getKeys({keyList: ['1', '2', 'esc'], waitRelease: false});
      _SDPracticeResp_allKeys = _SDPracticeResp_allKeys.concat(theseKeys);
      if (_SDPracticeResp_allKeys.length > 0) {
        SDPracticeResp.keys = _SDPracticeResp_allKeys[_SDPracticeResp_allKeys.length - 1].name;  // just the last key pressed
        SDPracticeResp.rt = _SDPracticeResp_allKeys[_SDPracticeResp_allKeys.length - 1].rt;
        // was this correct?
        if (SDPracticeResp.keys == corrAns) {
            SDPracticeResp.corr = 1;
        } else {
            SDPracticeResp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SDPracticeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SDPracticeRoutineEnd() {
  return async function () {
    //------Ending Routine 'SDPractice'-------
    SDPracticeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (SDPracticeResp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         SDPracticeResp.corr = 1;  // correct non-response
      } else {
         SDPracticeResp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('SDPracticeResp.keys', SDPracticeResp.keys);
    psychoJS.experiment.addData('SDPracticeResp.corr', SDPracticeResp.corr);
    if (typeof SDPracticeResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('SDPracticeResp.rt', SDPracticeResp.rt);
        routineTimer.reset();
        }
    
    SDPracticeResp.stop();
    // the Routine "SDPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var SDPracticeResponseComponents;
function SDPracticeResponseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'SDPracticeResponse'-------
    t = 0;
    SDPracticeResponseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.030000);
    // update component parameters for each repeat
    if (SDPracticeResp.corr) {
        feedbackPitch = soundfile[0];
    } else {
        feedbackPitch = soundfile[1];
    }
    
    feedback_3 = new sound.Sound({
    win: psychoJS.window,
    value: feedbackPitch,
    secs: 0.03,
    });
    feedback_3.secs=0.03;
    feedback_3.setVolume(1.0);
    // keep track of which components have finished
    SDPracticeResponseComponents = [];
    SDPracticeResponseComponents.push(feedback_3);
    
    SDPracticeResponseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SDPracticeResponseRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'SDPracticeResponse'-------
    // get current time
    t = SDPracticeResponseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop feedback_3
    if (t >= 0.0 && feedback_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_3.tStart = t;  // (not accounting for frame time here)
      feedback_3.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ feedback_3.play(); });  // screen flip
      feedback_3.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.03 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.03 > 0.5) {  feedback_3.stop();  // stop the sound (if longer than duration)
        feedback_3.status = PsychoJS.Status.FINISHED;
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SDPracticeResponseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SDPracticeResponseRoutineEnd() {
  return async function () {
    //------Ending Routine 'SDPracticeResponse'-------
    SDPracticeResponseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    feedback_3.stop();  // ensure sound has stopped at end of routine
    return Scheduler.Event.NEXT;
  };
}


var _SDTaskResp_allKeys;
var SDTaskInstComponents;
function SDTaskInstRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'SDTaskInst'-------
    t = 0;
    SDTaskInstClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    SDInstructrions.setAlignHoriz("left");
    SDInstructionArb.setAlignHoriz("right");
    
    SDTaskResp.keys = undefined;
    SDTaskResp.rt = undefined;
    _SDTaskResp_allKeys = [];
    // keep track of which components have finished
    SDTaskInstComponents = [];
    SDTaskInstComponents.push(SDTaskResp);
    SDTaskInstComponents.push(SDInstructrions);
    SDTaskInstComponents.push(SDInstructionArb);
    
    SDTaskInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SDTaskInstRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'SDTaskInst'-------
    // get current time
    t = SDTaskInstClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SDTaskResp* updates
    if (t >= 0.0 && SDTaskResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDTaskResp.tStart = t;  // (not accounting for frame time here)
      SDTaskResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SDTaskResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SDTaskResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { SDTaskResp.clearEvents(); });
    }

    if (SDTaskResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = SDTaskResp.getKeys({keyList: ['space'], waitRelease: false});
      _SDTaskResp_allKeys = _SDTaskResp_allKeys.concat(theseKeys);
      if (_SDTaskResp_allKeys.length > 0) {
        SDTaskResp.keys = _SDTaskResp_allKeys[_SDTaskResp_allKeys.length - 1].name;  // just the last key pressed
        SDTaskResp.rt = _SDTaskResp_allKeys[_SDTaskResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *SDInstructrions* updates
    if (t >= 0.0 && SDInstructrions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDInstructrions.tStart = t;  // (not accounting for frame time here)
      SDInstructrions.frameNStart = frameN;  // exact frame index
      
      SDInstructrions.setAutoDraw(true);
    }

    
    // *SDInstructionArb* updates
    if (t >= 0.0 && SDInstructionArb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDInstructionArb.tStart = t;  // (not accounting for frame time here)
      SDInstructionArb.frameNStart = frameN;  // exact frame index
      
      SDInstructionArb.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SDTaskInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SDTaskInstRoutineEnd() {
  return async function () {
    //------Ending Routine 'SDTaskInst'-------
    SDTaskInstComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    SDTaskResp.stop();
    // the Routine "SDTaskInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _SDResp_allKeys;
var SDTaskComponents;
function SDTaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'SDTask'-------
    t = 0;
    SDTaskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    g = util.randint(0, 2);
    if ((g === 1)) {
        stim1 = word1;
        stim2 = word2;
        xstim1 = xword1;
        ystim1 = yword1;
        xstim2 = xword2;
        ystim2 = yword2;
        xstim1_D = xword1_D;
        ystim1_D = yword1_D;
        xstim2_D = xword2_D;
        ystim2_D = yword2_D;
        stim1_D = word1_D;
        stim2_D = word2_D;
    } else {
        stim1 = word2;
        stim2 = word1;
        xstim1 = xword2;
        ystim1 = yword2;
        xstim2 = xword1;
        ystim2 = yword1;
        xstim1_D = xword2_D;
        ystim1_D = yword2_D;
        xstim2_D = xword1_D;
        ystim2_D = yword1_D;
        stim1_D = word2_D;
        stim2_D = word1_D;
    }
    
    SDWord1.setPos([xstim1, ystim1]);
    SDWord1.setText(stim1);
    SDDist1.setPos([xstim1_D, ystim1_D]);
    SDDist1.setText(stim1_D);
    cue_4.setPos([xstim1, (- 0.11)]);
    noiseImage_4.setPos([xstim1, ystim1]);
    noiseImage_D_4.setPos([xstim1_D, ystim1_D]);
    SDWord2.setPos([xstim2, ystim2]);
    SDWord2.setText(stim2);
    SDDist2.setPos([xstim2_D, ystim2_D]);
    SDDist2.setText(stim2_D);
    cue_5.setPos([xstim2, (- 0.11)]);
    SDResp.keys = undefined;
    SDResp.rt = undefined;
    _SDResp_allKeys = [];
    // keep track of which components have finished
    SDTaskComponents = [];
    SDTaskComponents.push(SDFixation_2);
    SDTaskComponents.push(SDWord1);
    SDTaskComponents.push(SDDist1);
    SDTaskComponents.push(cue_4);
    SDTaskComponents.push(noiseImage_4);
    SDTaskComponents.push(noiseImage_D_4);
    SDTaskComponents.push(SDWord2);
    SDTaskComponents.push(SDDist2);
    SDTaskComponents.push(cue_5);
    SDTaskComponents.push(SDResp);
    
    SDTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SDTaskRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'SDTask'-------
    // get current time
    t = SDTaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    /* Syntax Error: Fix Python code */
    
    // *SDFixation_2* updates
    if (t >= 0.3 && SDFixation_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDFixation_2.tStart = t;  // (not accounting for frame time here)
      SDFixation_2.frameNStart = frameN;  // exact frame index
      
      SDFixation_2.setAutoDraw(true);
    }

    
    // *SDWord1* updates
    if (t >= 0.6 && SDWord1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDWord1.tStart = t;  // (not accounting for frame time here)
      SDWord1.frameNStart = frameN;  // exact frame index
      
      SDWord1.setAutoDraw(true);
    }

    frameRemains = 0.6 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (SDWord1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      SDWord1.setAutoDraw(false);
    }
    
    // *SDDist1* updates
    if (t >= 0.6 && SDDist1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDDist1.tStart = t;  // (not accounting for frame time here)
      SDDist1.frameNStart = frameN;  // exact frame index
      
      SDDist1.setAutoDraw(true);
    }

    frameRemains = 0.6 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (SDDist1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      SDDist1.setAutoDraw(false);
    }
    
    // *cue_4* updates
    if (t >= 0.6 && cue_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cue_4.tStart = t;  // (not accounting for frame time here)
      cue_4.frameNStart = frameN;  // exact frame index
      
      cue_4.setAutoDraw(true);
    }

    frameRemains = 0.6 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cue_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cue_4.setAutoDraw(false);
    }
    
    // *noiseImage_4* updates
    if (t >= 0.8 && noiseImage_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noiseImage_4.tStart = t;  // (not accounting for frame time here)
      noiseImage_4.frameNStart = frameN;  // exact frame index
      
      noiseImage_4.setAutoDraw(true);
    }

    frameRemains = 0.8 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (noiseImage_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      noiseImage_4.setAutoDraw(false);
    }
    
    // *noiseImage_D_4* updates
    if (t >= 0.8 && noiseImage_D_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noiseImage_D_4.tStart = t;  // (not accounting for frame time here)
      noiseImage_D_4.frameNStart = frameN;  // exact frame index
      
      noiseImage_D_4.setAutoDraw(true);
    }

    frameRemains = 0.8 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (noiseImage_D_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      noiseImage_D_4.setAutoDraw(false);
    }
    
    // *SDWord2* updates
    if (t >= 1.0 && SDWord2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDWord2.tStart = t;  // (not accounting for frame time here)
      SDWord2.frameNStart = frameN;  // exact frame index
      
      SDWord2.setAutoDraw(true);
    }

    frameRemains = 1.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (SDWord2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      SDWord2.setAutoDraw(false);
    }
    
    // *SDDist2* updates
    if (t >= 1.0 && SDDist2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDDist2.tStart = t;  // (not accounting for frame time here)
      SDDist2.frameNStart = frameN;  // exact frame index
      
      SDDist2.setAutoDraw(true);
    }

    frameRemains = 1.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (SDDist2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      SDDist2.setAutoDraw(false);
    }
    
    // *cue_5* updates
    if (t >= 1.0 && cue_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cue_5.tStart = t;  // (not accounting for frame time here)
      cue_5.frameNStart = frameN;  // exact frame index
      
      cue_5.setAutoDraw(true);
    }

    frameRemains = 1.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cue_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cue_5.setAutoDraw(false);
    }
    
    // *SDResp* updates
    if (t >= 1.0 && SDResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDResp.tStart = t;  // (not accounting for frame time here)
      SDResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SDResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SDResp.start(); }); // start on screen flip
    }

    if (SDResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = SDResp.getKeys({keyList: ['1', '2', 'esc'], waitRelease: false});
      _SDResp_allKeys = _SDResp_allKeys.concat(theseKeys);
      if (_SDResp_allKeys.length > 0) {
        SDResp.keys = _SDResp_allKeys[_SDResp_allKeys.length - 1].name;  // just the last key pressed
        SDResp.rt = _SDResp_allKeys[_SDResp_allKeys.length - 1].rt;
        // was this correct?
        if (SDResp.keys == corrAns) {
            SDResp.corr = 1;
        } else {
            SDResp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SDTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SDTaskRoutineEnd() {
  return async function () {
    //------Ending Routine 'SDTask'-------
    SDTaskComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (SDResp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         SDResp.corr = 1;  // correct non-response
      } else {
         SDResp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('SDResp.keys', SDResp.keys);
    psychoJS.experiment.addData('SDResp.corr', SDResp.corr);
    if (typeof SDResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('SDResp.rt', SDResp.rt);
        routineTimer.reset();
        }
    
    SDResp.stop();
    // the Routine "SDTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var SDResponseComponents;
function SDResponseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'SDResponse'-------
    t = 0;
    SDResponseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.030000);
    // update component parameters for each repeat
    if (SDResp.corr) {
        feedbackPitch = soundfile[0];
    } else {
        feedbackPitch = soundfile[1];
    }
    
    feedback_4 = new sound.Sound({
    win: psychoJS.window,
    value: feedbackPitch,
    secs: 0.03,
    });
    feedback_4.secs=0.03;
    feedback_4.setVolume(1.0);
    // keep track of which components have finished
    SDResponseComponents = [];
    SDResponseComponents.push(feedback_4);
    
    SDResponseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SDResponseRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'SDResponse'-------
    // get current time
    t = SDResponseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop feedback_4
    if (t >= 0.0 && feedback_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_4.tStart = t;  // (not accounting for frame time here)
      feedback_4.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ feedback_4.play(); });  // screen flip
      feedback_4.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.03 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.03 > 0.5) {  feedback_4.stop();  // stop the sound (if longer than duration)
        feedback_4.status = PsychoJS.Status.FINISHED;
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SDResponseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SDResponseRoutineEnd() {
  return async function () {
    //------Ending Routine 'SDResponse'-------
    SDResponseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    feedback_4.stop();  // ensure sound has stopped at end of routine
    return Scheduler.Event.NEXT;
  };
}


var _SDBreakResp_allKeys;
var SDBreakComponents;
function SDBreakRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'SDBreak'-------
    t = 0;
    SDBreakClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    endOfSD.setAlignHoriz("left");
    endOfSDArb.setAlignHoriz("right");
    
    SDBreakResp.keys = undefined;
    SDBreakResp.rt = undefined;
    _SDBreakResp_allKeys = [];
    // keep track of which components have finished
    SDBreakComponents = [];
    SDBreakComponents.push(SDBreakResp);
    SDBreakComponents.push(endOfSD);
    SDBreakComponents.push(endOfSDArb);
    
    SDBreakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SDBreakRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'SDBreak'-------
    // get current time
    t = SDBreakClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SDBreakResp* updates
    if (t >= 0.0 && SDBreakResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SDBreakResp.tStart = t;  // (not accounting for frame time here)
      SDBreakResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SDBreakResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SDBreakResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { SDBreakResp.clearEvents(); });
    }

    if (SDBreakResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = SDBreakResp.getKeys({keyList: ['space'], waitRelease: false});
      _SDBreakResp_allKeys = _SDBreakResp_allKeys.concat(theseKeys);
      if (_SDBreakResp_allKeys.length > 0) {
        SDBreakResp.keys = _SDBreakResp_allKeys[_SDBreakResp_allKeys.length - 1].name;  // just the last key pressed
        SDBreakResp.rt = _SDBreakResp_allKeys[_SDBreakResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *endOfSD* updates
    if (t >= 0.0 && endOfSD.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endOfSD.tStart = t;  // (not accounting for frame time here)
      endOfSD.frameNStart = frameN;  // exact frame index
      
      endOfSD.setAutoDraw(true);
    }

    
    // *endOfSDArb* updates
    if (t >= 0.0 && endOfSDArb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endOfSDArb.tStart = t;  // (not accounting for frame time here)
      endOfSDArb.frameNStart = frameN;  // exact frame index
      
      endOfSDArb.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SDBreakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SDBreakRoutineEnd() {
  return async function () {
    //------Ending Routine 'SDBreak'-------
    SDBreakComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SDBreakResp.keys', SDBreakResp.keys);
    if (typeof SDBreakResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('SDBreakResp.rt', SDBreakResp.rt);
        routineTimer.reset();
        }
    
    SDBreakResp.stop();
    // the Routine "SDBreak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
