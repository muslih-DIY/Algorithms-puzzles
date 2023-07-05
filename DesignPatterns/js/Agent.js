
function currentfunction() {
    const error = new Error();
    const stack = error.stack.split('\n');
    return stack[2].trim().split(' ')[1].split('.')[1];

  }

// State interface
class AgentState {
    constructor(name,agent) {
      this.agent = agent;
      this.name = name
    }
    onEnter(){
        
        log(`<span style="color:green"> entering .. into ${this.name}</span>`);

    }
    onExit(){
        log(`<span style="color:blue">Exiting .. from  ${this.name} </span>`);
    }
    logAction(fn){
        log(`from state <strong>${this.name}, ${fn}</strong> action performed `);
    }
    warngin(content){
        log(`<span style="color:orange">state <strong>${this.name}: ${content} state</strong></span>`);
    }
    notallowed(agent,fn){
        log(`<span style="color:red">This Action (${fn} )is not allowed in the "${this.agent.currentState.name}" state</span>`);
    }
    enterCampaign(agent) {
        // enter into the campaign
        this.notallowed(agent);
        
    }
    exitCampaign(agent) {
        this.notallowed(agent,currentfunction());
    }
    login(agent) {
        this.notallowed(agent,currentfunction());
    }
    logout(agent){
        this.notallowed(agent,currentfunction());

    }
    reject(agent) {
        this.notallowed(agent,currentfunction());
    }
    accept(agent) {
        this.notallowed(agent,currentfunction());
    }
    pause(agent) {
        this.notallowed(agent,currentfunction());
    }
    unpause(agent) {
        this.notallowed(agent,currentfunction());
    }
    hold(agent) {
        this.notallowed(agent,currentfunction());
    }
    unhold(agent) {
        this.notallowed(agent,currentfunction());
    }
    hangup(agent) {
        this.notallowed(agent,currentfunction());
    }

  }
  
  
  // Concrete state classes

  

  class LoggedOutState extends AgentState {
    constructor(agent) {
      super('Logged Out',agent);
    }
    login(agent) {
        this.agent.enterState(this.agent.loggedInState);
    }
  }
  
  class LoggedInState extends AgentState {
    constructor(agent) {
      super('LoggedIn',agent);
    }
    enterCampaign(agent) {
      this.agent.enterState(this.agent.readyState);
    }
    logout(){
        this.agent.enterState(this.agent.loggedInState);
    }

    
  }

  class ReadyState extends AgentState {
    constructor(agent){
        super('Ready',agent);
    }
    exitCampaign(){
        this.agent.enterState(this.agent.loggedInState);
    }
    pause(){
        this.agent.enterState(this.agent.pausedState);
        
    }
    logout(){
        this.agent.exitCampaign();
        this.agent.enterState(this.agent.loggedOutState);
    }
    enterCampaign(){
        this.warngin("Already on ReadyState");
    }

  }
  
  class InCallState extends AgentState {
    constructor(agent) {
      super('InCall',agent);
    }
    hold(agent) {
        this.agent.enterState(this.agent.holdState);
    }
    hangup(agent) {
        this.agent.enterState(this.agent.readyState);

    }
  }

  class PausedState extends AgentState{
    constructor(agent){
        super('Paused',agent);
    }

    pause(){
        this.warngin("Already in the paused state");
    }
    unpause(){
        this.agent.enterState(this.agent.readyState);
    }
    exitCampaign(){
        this.unpause();
        //now at ready state
        this.agent.exitCampaign();
    }
    logout(){
        this.unpause();
        // now at ready state
        this.agent.logout();
    }
  }
  
  class RingingState extends AgentState{
    constructor(agent){
        super('Ringing',agent);
    }
    onEnter(){
        super.onEnter();
    }
    accept(){
        this.agent.enterState(this.agent.inCallState);
    }
    reject(){
        this.agent.enterState(this.agent.readyState);
    }
  }
  
  class HoldState extends AgentState {
    constructor(agent) {
      super('OnHold',agent);
    }

    unhold(agent) {
        this.agent.enterState(this.agent.inCallState);
    }
  }
  
  // Context class
  class Agent {
    constructor(agent) {
      this.loggedInState = new LoggedInState(this);
      this.ringingState = new RingingState(this);
      this.readyState = new ReadyState(this);
      this.pausedState = new PausedState(this);
      this.inCallState = new InCallState(this);
      this.holdState = new HoldState(this);
      this.loggedOutState = new LoggedOutState(this);
  
      this.currentState = this.loggedInState;
    }
  
    setState(state) {
      this.currentState = state;
    }

    exitState(){
        this.currentState.onExit();
    }
    enterState(state){
        this.exitState();
        this.setState(state);
        this.currentState.onEnter();
    }
 
  
    login() {
        this.currentState.logAction(currentfunction());
        this.currentState.login();
    }

    enterCampaign(){
        this.currentState.logAction(currentfunction());
        this.currentState.enterCampaign();
    }
  
    exitCampaign(){
        this.currentState.logAction(currentfunction());
        this.currentState.exitCampaign();
    }

  
    pause() {
        this.currentState.logAction(currentfunction());
        this.currentState.pause();
    }

    unpause(){
        this.currentState.logAction(currentfunction());
        this.currentState.unpause();
    }
    hold(){
        this.currentState.logAction(currentfunction());
        this.currentState.hold();
    
    }
    unhold(){
        this.currentState.logAction(currentfunction());
        this.currentState.unhold();
    }
    accept(){
        this.currentState.logAction(currentfunction());
        this.currentState.accept();
    }
    reject(){
        this.currentState.logAction(currentfunction());
        this.currentState.reject();
    }
    hangup(){
        this.currentState.logAction(currentfunction());
        this.currentState.hangup();
    }
    logout(){
        this.currentState.logAction(currentfunction());
        this.currentState.logout();  
    }
    force_logout(){
        this.currentState.logAction(currentfunction());
        switch(this.currentState){
            case this.inCallState:
                this.hangup();
                break;
            case this.holdState:
                this.unhold();
                this.hangup();
            default:

        }
        this.enterState(this.loggedInState);
        this.enterState(this.loggedOutState);
    }
  }
  
  function log(x){
    document.write(x+'<br>');
    console.log(x);
  }

  function do_all_action(agent){
    agent.enterCampaign();
    agent.accept();
    agent.reject();
    agent.hold();
    agent.unhold();
    agent.pause();
    agent.unpause();
    agent.hangup();
    agent.exitCampaign();
    agent.login();
    agent.logout();
  }
  const agent = new Agent();
  log('<h2>current state: '+agent.currentState.name+'</h2>');
  do_all_action(agent);
  agent.enterCampaign();
  log('<h2>current state: '+agent.currentState.name+'</h2>');
  do_all_action(agent); 
  log('<h2>current state: '+agent.currentState.name+'</h2>');
  agent.enterCampaign();
  agent.pause();
  log('<h2>current state: '+agent.currentState.name+'</h2>');

  agent.enterState(agent.ringingState);

  log('<h2>current state: '+agent.currentState.name+'</h2>');
  agent.hold();
  agent.unhold();
  agent.hangup();
  agent.pause();
  agent.logout();
  agent.unpause();
  agent.reject();
  agent.enterState(agent.ringingState);
  log('<h2>current state: '+agent.currentState.name+'</h2>');
  agent.accept();
  agent.reject();
  agent.hold();
  agent.pause();
  agent.logout();
  agent.exitCampaign();
  agent.hangup();
  agent.unhold();
  agent.hangup();
  log('<h2>current state: '+agent.currentState.name+'</h2>');
  agent.logout();
  agent.login();
  agent.enterCampaign();
  agent.force_logout();
  agent.login();
  agent.pause();
  agent.enterCampaign();
  agent.pause();
  agent.logout();
  agent.login();
  agent.enterCampaign();
  agent.enterState(agent.ringingState);
  log('<h2>current state: '+agent.currentState.name+'</h2>');
  agent.logout();
  agent.force_logout();

  agent.enterState(agent.ringingState);
  log('<h2>current state: '+agent.currentState.name+'</h2>');
  agent.accept();
  agent.logout();
  agent.hold();
  agent.accept();
  agent.force_logout();
  
  agent.enterState(agent.ringingState);
  log('<h2>current state: '+agent.currentState.name+'</h2>');
  agent.accept();
  agent.force_logout();