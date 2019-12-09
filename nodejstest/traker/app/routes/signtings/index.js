import Route from '@ember/routing/route';

export default Route.extend({
  model(){
    //return [
    //  {id:1, location:'tianjin', signtedAt: new Date('2019-03-07')},
    //  {id:2, location:'beijing', signtedAt: new Date('2019-03-08')},
    //  {id:3, location:'henan', signtedAt: new Date('2019-03-09')},
    //  {id:4, location:'hunan', signtedAt: new Date('2019-03-10')}
    //]
    //
    let r1 = this.store.createRecord('signting', {location:'tianjin', signtedAt: new Date('2019-03-07')});
    console.log('record 1 location ' + r1.get('location'));
    r1.set('location', 'hunan');
    console.log('record 1 location ' + r1.get('location'));
    let r2 = this.store.createRecord('signting', {location:'beijing', signtedAt: new Date('2019-03-08')});
    let r3 = this.store.createRecord('signting', {location:'henan', signtedAt: new Date('2019-03-09')});
    return [r1, r2, r3];
  }
});
