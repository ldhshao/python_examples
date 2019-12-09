import Route from '@ember/routing/route';

export default Route.extend({
  model(){
    let w1 = this.store.createRecord('witness', {fName:'donghao', lName:'liu', email:'liu198456@126.com'});
    return [w1];
  }
});
