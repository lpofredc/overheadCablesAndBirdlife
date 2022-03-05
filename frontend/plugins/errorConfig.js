/**
 * This file contains the errorcode configuration for the app.
 *
 * code: it is error code determined for this app.
 * Values start at 701 to avoid confusion with HTTP statusCodes.
 * Error capture in nuxt do not contains "statusError" property, only "message" property
 * This "message" property is not provided to user.
 *
 * msg: it is message provided when the error occures. The chain matches to chain used by i18n
 * (internationalization). Refer in '~/locales/*'.
 */
errorCodes = {
  // refer login-component (ID/Password error)
  authentication: {
    code: 401,
    msg: 'id-pwd-issue',
  },
  // refer login-component
  login: {
    code: 601,
    msg: 'login-issue',
  },
  // refer loadNomenclatures in nomenclatureStore
  nomenclature_not_found: {
    code: 701,
    msg: 'nomenclature_not_found_resource',
  },
  // refer loadNomenclatures in nomenclatureStore
  loading_whole_nomenclatures: {
    code: 702,
    msg: 'loading-issue',
  },
  // refer getConditions in nomenclatureStore
  get_infrstr_conditions: {
    code: 703,
    msg: 'loading-issue',
  },
  // refer getOwners in nomenclatureStore
  get_infrstr_owners: {
    code: 704,
    msg: 'loading-issue',
  },
  // refer getPoleTypes in nomenclatureStore
  get_infrstr_poletypes: {
    code: 705,
    msg: 'loading-issue',
  },
  // refer getPoleTypes in nomenclatureStore
  get_infrstr_risklevels: {
    code: 706,
    msg: 'loading-issue',
  },
  // refer submit in point-component
  create_pole: {
    code: 801,
    msg: 'create-issue',
  },
}
