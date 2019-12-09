import Model, {attr, hasMany, belongsTo} from '@ember-data/model';

export default Model.extend({
  location: attr('string'),
  signtedAt: attr('date'),
  createdAt: attr('date'),
  cryptid: belongsTo('cryptid'),
  witnesses: hasMany('witness')
});
