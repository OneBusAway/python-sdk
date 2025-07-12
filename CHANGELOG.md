# Changelog

## 1.13.5 (2025-07-12)

Full Changelog: [v1.13.4...v1.13.5](https://github.com/OneBusAway/python-sdk/compare/v1.13.4...v1.13.5)

### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([935e2d2](https://github.com/OneBusAway/python-sdk/commit/935e2d25ec8736de5b30d7653c2e85fd5620a45d))


### Chores

* **readme:** fix version rendering on pypi ([e29e75d](https://github.com/OneBusAway/python-sdk/commit/e29e75dcc69ffc9b0c434cf556cfa9b5b374d7a4))

## 1.13.4 (2025-07-10)

Full Changelog: [v1.13.3...v1.13.4](https://github.com/OneBusAway/python-sdk/compare/v1.13.3...v1.13.4)

### Bug Fixes

* **parsing:** correctly handle nested discriminated unions ([d1bb078](https://github.com/OneBusAway/python-sdk/commit/d1bb078b61f81f9f5192505e08cea3dc7df136f4))

## 1.13.3 (2025-07-09)

Full Changelog: [v1.13.2...v1.13.3](https://github.com/OneBusAway/python-sdk/compare/v1.13.2...v1.13.3)

### Chores

* **internal:** bump pinned h11 dep ([495b65d](https://github.com/OneBusAway/python-sdk/commit/495b65dad98321a877258bdd87872357c245f9cf))
* **package:** mark python 3.13 as supported ([404807c](https://github.com/OneBusAway/python-sdk/commit/404807c5890115889c90bc1236f9ca0b57a426c8))

## 1.13.2 (2025-07-05)

Full Changelog: [v1.13.1...v1.13.2](https://github.com/OneBusAway/python-sdk/compare/v1.13.1...v1.13.2)

### Chores

* **internal:** version bump ([b017c04](https://github.com/OneBusAway/python-sdk/commit/b017c04d3b411ec13e528851f32c850839c3274d))

## 1.13.1 (2025-07-02)

Full Changelog: [v1.13.0...v1.13.1](https://github.com/OneBusAway/python-sdk/compare/v1.13.0...v1.13.1)

### Bug Fixes

* **ci:** correct conditional ([1b938b2](https://github.com/OneBusAway/python-sdk/commit/1b938b23923b4ee59453b26a896747bd7f4d0386))


### Chores

* **ci:** change upload type ([add541c](https://github.com/OneBusAway/python-sdk/commit/add541c1c196ef11b5ae310d0944b39f476915b0))
* **ci:** only run for pushes and fork pull requests ([e15aec6](https://github.com/OneBusAway/python-sdk/commit/e15aec647d9bdbcbd061158740afa8df57f0d41c))

## 1.13.0 (2025-06-27)

Full Changelog: [v1.12.2...v1.13.0](https://github.com/OneBusAway/python-sdk/compare/v1.12.2...v1.13.0)

### Features

* **client:** add support for aiohttp ([30eada9](https://github.com/OneBusAway/python-sdk/commit/30eada97ab7083d960307901bb55ef931ff6b202))


### Bug Fixes

* **ci:** release-doctor — report correct token name ([32bbbb3](https://github.com/OneBusAway/python-sdk/commit/32bbbb36efc1e3ebe55502aba1d140b0670e671c))


### Chores

* **tests:** skip some failing tests on the latest python versions ([6a88517](https://github.com/OneBusAway/python-sdk/commit/6a88517328513ff342df314e1d1da26795f3bb72))

## 1.12.2 (2025-06-19)

Full Changelog: [v1.12.1...v1.12.2](https://github.com/OneBusAway/python-sdk/compare/v1.12.1...v1.12.2)

### Bug Fixes

* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([355779a](https://github.com/OneBusAway/python-sdk/commit/355779aceef53b58275a4dab5020d414044adbb0))


### Chores

* **ci:** enable for pull requests ([2b9118f](https://github.com/OneBusAway/python-sdk/commit/2b9118f1154e0f8e90c71a1fb37577c63a57c63f))
* **internal:** update conftest.py ([a2b6c3e](https://github.com/OneBusAway/python-sdk/commit/a2b6c3e1d78656155c5eb2f0a1cff69de045909b))
* **readme:** update badges ([dc50499](https://github.com/OneBusAway/python-sdk/commit/dc504994e1f2c2c76e0a46941b97b35a90b0e5c5))
* **tests:** add tests for httpx client instantiation & proxies ([55c4719](https://github.com/OneBusAway/python-sdk/commit/55c4719837747d638cfbb9e79f683189045338ab))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([5e8cb3a](https://github.com/OneBusAway/python-sdk/commit/5e8cb3aa66d4a60f7e96d71cf5bbf2fedeb172ef))

## 1.12.1 (2025-06-13)

Full Changelog: [v1.12.0...v1.12.1](https://github.com/OneBusAway/python-sdk/compare/v1.12.0...v1.12.1)

### Bug Fixes

* **client:** correctly parse binary response | stream ([4bc049c](https://github.com/OneBusAway/python-sdk/commit/4bc049ce0a36680434f5570fd38f3ca673250bba))


### Chores

* **tests:** run tests in parallel ([1329bbe](https://github.com/OneBusAway/python-sdk/commit/1329bbe39e76943fe51efea63dc5ee7f85154135))

## 1.12.0 (2025-06-03)

Full Changelog: [v1.11.1...v1.12.0](https://github.com/OneBusAway/python-sdk/compare/v1.11.1...v1.12.0)

### Features

* **client:** add follow_redirects request option ([569c63a](https://github.com/OneBusAway/python-sdk/commit/569c63a79d7d69d4e7f54466860e462114385db9))


### Chores

* **docs:** remove reference to rye shell ([064f5b8](https://github.com/OneBusAway/python-sdk/commit/064f5b86a6b67b49431886f2892cdfb6cd221e8a))

## 1.11.1 (2025-05-22)

Full Changelog: [v1.11.0...v1.11.1](https://github.com/OneBusAway/python-sdk/compare/v1.11.0...v1.11.1)

### Chores

* **docs:** grammar improvements ([052af65](https://github.com/OneBusAway/python-sdk/commit/052af65693c380484e4e920b4a831c52b4345daa))

## 1.11.0 (2025-05-20)

Full Changelog: [v1.10.0...v1.11.0](https://github.com/OneBusAway/python-sdk/compare/v1.10.0...v1.11.0)

### Features

* **api:** api update ([9981b15](https://github.com/OneBusAway/python-sdk/commit/9981b15b92023faad9812c2ad55f977673424c1b))

## 1.10.0 (2025-05-17)

Full Changelog: [v1.9.1...v1.10.0](https://github.com/OneBusAway/python-sdk/compare/v1.9.1...v1.10.0)

### Features

* **api:** api update ([e1770ea](https://github.com/OneBusAway/python-sdk/commit/e1770ea404333e965948a7e27bec57215985c82d))

## 1.9.1 (2025-05-16)

Full Changelog: [v1.9.0...v1.9.1](https://github.com/OneBusAway/python-sdk/compare/v1.9.0...v1.9.1)

### Chores

* **internal:** codegen related update ([d996edf](https://github.com/OneBusAway/python-sdk/commit/d996edfce7df8c642feda6c88a46e3e9638e2364))

## 1.9.0 (2025-05-15)

Full Changelog: [v1.8.6...v1.9.0](https://github.com/OneBusAway/python-sdk/compare/v1.8.6...v1.9.0)

### Features

* **client:** support digest authentication ([7968d8e](https://github.com/OneBusAway/python-sdk/commit/7968d8ec213da1e0f7c6006a262f4490d33dc189))
* **client:** support digest authentication ([645fab1](https://github.com/OneBusAway/python-sdk/commit/645fab1f917aa2911f8a202962c14497703a6e4a))
* **client:** support digest authentication ([442412c](https://github.com/OneBusAway/python-sdk/commit/442412cf7414b96fcc111b099b0899be6dda2c62))
* **client:** support digest authentication ([78752fb](https://github.com/OneBusAway/python-sdk/commit/78752fb2e2757500df6fbe2243f8c958d21d45b1))


### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([0bf5ca2](https://github.com/OneBusAway/python-sdk/commit/0bf5ca29079b4844d824aeffa45701d453aee07f))
* suppress type checking warnings in stops_for_location.py ([6f86de6](https://github.com/OneBusAway/python-sdk/commit/6f86de60f85548d408891725075ac596b6a756f5))


### Chores

* broadly detect json family of content-type headers ([4ac9df4](https://github.com/OneBusAway/python-sdk/commit/4ac9df4564811ba3a7874ed2fccdcedf0ee9f926))
* **ci:** add timeout thresholds for CI jobs ([4f9bf3f](https://github.com/OneBusAway/python-sdk/commit/4f9bf3f56e7a4121c02d0b42940758c5ee8d15a9))
* **ci:** only use depot for staging repos ([b943cd6](https://github.com/OneBusAway/python-sdk/commit/b943cd6d8a741d5b0eb46f0e3f071c05243d7a96))
* **client:** minor internal fixes ([46ef2ca](https://github.com/OneBusAway/python-sdk/commit/46ef2ca789d1cda13173d4cb9eb13cd45926436d))
* formatting ([3a1f625](https://github.com/OneBusAway/python-sdk/commit/3a1f6255316b831eec27a42deecfd7a51d55bb24))
* **internal:** base client updates ([5dcff0e](https://github.com/OneBusAway/python-sdk/commit/5dcff0e41a90577caf12e799b9388e88661afdaf))
* **internal:** bump pyright version ([372d33b](https://github.com/OneBusAway/python-sdk/commit/372d33b378a44bc1f7a37282c7c5a6617978b105))
* **internal:** codegen related update ([f2c26ec](https://github.com/OneBusAway/python-sdk/commit/f2c26ec71b462bee6c57253056c2e35ac26bea59))
* **internal:** fix list file params ([2401f32](https://github.com/OneBusAway/python-sdk/commit/2401f32e86b394778db413a97be0ece06ea34346))
* **internal:** import reformatting ([55369d4](https://github.com/OneBusAway/python-sdk/commit/55369d4913d0db14d4f8a5f0b177513e29c49246))
* **internal:** minor formatting changes ([769fecb](https://github.com/OneBusAway/python-sdk/commit/769fecb626b4d8c82b26d156a5583c635c8471f9))
* **internal:** refactor retries to not use recursion ([f034ad2](https://github.com/OneBusAway/python-sdk/commit/f034ad2291495dc12c523e297f7871cf4bdccc42))
* **internal:** update models test ([6d50ec1](https://github.com/OneBusAway/python-sdk/commit/6d50ec101d12998985b8b3559a2ae06d9f9f8f91))
* **internal:** update pyright settings ([2583fea](https://github.com/OneBusAway/python-sdk/commit/2583feac4ae8ea9a480be9694dd1bbfbf36c8e24))

## 1.8.6 (2025-05-15)

Full Changelog: [v1.8.5...v1.8.6](https://github.com/OneBusAway/python-sdk/compare/v1.8.5...v1.8.6)

### Bug Fixes

* **perf:** optimize some hot paths ([ddf06ce](https://github.com/OneBusAway/python-sdk/commit/ddf06ce0964f841e82a46417d233bc309740e169))
* **perf:** skip traversing types for NotGiven values ([3ef7f7b](https://github.com/OneBusAway/python-sdk/commit/3ef7f7b6a016058d1d68e912d12e81e4c7b8f10f))


### Chores

* **internal:** codegen related update ([#290](https://github.com/OneBusAway/python-sdk/issues/290)) ([ae2f18c](https://github.com/OneBusAway/python-sdk/commit/ae2f18c4204970d2f5021b0060c6be7c562dfb54))
* **internal:** expand CI branch coverage ([3ba0a52](https://github.com/OneBusAway/python-sdk/commit/3ba0a52f74ffdc7b0cabdf2dfdd44537c132dc06))
* **internal:** reduce CI branch coverage ([c2e056e](https://github.com/OneBusAway/python-sdk/commit/c2e056e95068b3ffb80279d69b5a7603ffbc256c))
* **internal:** slight transform perf improvement ([#291](https://github.com/OneBusAway/python-sdk/issues/291)) ([f74def5](https://github.com/OneBusAway/python-sdk/commit/f74def5e32618dc6ff2fb364cad51c01940af849))

## 1.8.5 (2025-05-15)

Full Changelog: [v1.8.4...v1.8.5](https://github.com/OneBusAway/python-sdk/compare/v1.8.4...v1.8.5)

### Chores

* **internal:** codegen related update ([#288](https://github.com/OneBusAway/python-sdk/issues/288)) ([d301a0c](https://github.com/OneBusAway/python-sdk/commit/d301a0cf24104ff0d791046c99093f3c47365bf3))

## 1.8.4 (2025-03-27)

Full Changelog: [v1.8.3...v1.8.4](https://github.com/OneBusAway/python-sdk/compare/v1.8.3...v1.8.4)

### Bug Fixes

* **ci:** ensure pip is always available ([#284](https://github.com/OneBusAway/python-sdk/issues/284)) ([959d15e](https://github.com/OneBusAway/python-sdk/commit/959d15edcf912b2742e3598a35396041492ecbb7))
* **ci:** remove publishing patch ([#285](https://github.com/OneBusAway/python-sdk/issues/285)) ([43691e0](https://github.com/OneBusAway/python-sdk/commit/43691e0b16c2c885b8e75d07e82f1ff26d961ac8))
* **types:** handle more discriminated union shapes ([#283](https://github.com/OneBusAway/python-sdk/issues/283)) ([d55c08a](https://github.com/OneBusAway/python-sdk/commit/d55c08ad0ff636bf899c7a989185f30f431649bb))


### Chores

* fix typos ([#286](https://github.com/OneBusAway/python-sdk/issues/286)) ([e45e047](https://github.com/OneBusAway/python-sdk/commit/e45e04798e64b912d4ba598ebc3ef0cdaf031203))
* **internal:** bump rye to 0.44.0 ([#282](https://github.com/OneBusAway/python-sdk/issues/282)) ([217ce3f](https://github.com/OneBusAway/python-sdk/commit/217ce3f97be80d4861ffc277336ec196c6873788))
* **internal:** remove extra empty newlines ([#280](https://github.com/OneBusAway/python-sdk/issues/280)) ([3ca5c73](https://github.com/OneBusAway/python-sdk/commit/3ca5c734669aad9252aca2761537f2cf6dc9cfab))

## 1.8.3 (2025-03-04)

Full Changelog: [v1.8.2...v1.8.3](https://github.com/OneBusAway/python-sdk/compare/v1.8.2...v1.8.3)

### Chores

* **docs:** update client docstring ([#274](https://github.com/OneBusAway/python-sdk/issues/274)) ([cd68881](https://github.com/OneBusAway/python-sdk/commit/cd68881b35a8a1d83ff1de64bca8e8dea8494ebd))
* **internal:** remove unused http client options forwarding ([#276](https://github.com/OneBusAway/python-sdk/issues/276)) ([7b2e2e5](https://github.com/OneBusAway/python-sdk/commit/7b2e2e505c7d440daa02464839512ee309113b02))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#273](https://github.com/OneBusAway/python-sdk/issues/273)) ([362a2f9](https://github.com/OneBusAway/python-sdk/commit/362a2f95e074ad28da196fc58a10df96ca7bc9e9))

## 1.8.2 (2025-02-26)

Full Changelog: [v1.8.1...v1.8.2](https://github.com/OneBusAway/python-sdk/compare/v1.8.1...v1.8.2)

### Chores

* **internal:** properly set __pydantic_private__ ([#270](https://github.com/OneBusAway/python-sdk/issues/270)) ([b14c2b5](https://github.com/OneBusAway/python-sdk/commit/b14c2b5b6f6bf376fcf0aeb6c3ae0536a222c131))

## 1.8.1 (2025-02-22)

Full Changelog: [v1.8.0...v1.8.1](https://github.com/OneBusAway/python-sdk/compare/v1.8.0...v1.8.1)

### Chores

* **internal:** fix devcontainers setup ([#267](https://github.com/OneBusAway/python-sdk/issues/267)) ([aaa9050](https://github.com/OneBusAway/python-sdk/commit/aaa9050c599ae62cfa24ba579c5a6b864a7adb73))

## 1.8.0 (2025-02-21)

Full Changelog: [v1.7.1...v1.8.0](https://github.com/OneBusAway/python-sdk/compare/v1.7.1...v1.8.0)

### Features

* **client:** allow passing `NotGiven` for body ([#264](https://github.com/OneBusAway/python-sdk/issues/264)) ([a4b3083](https://github.com/OneBusAway/python-sdk/commit/a4b3083b2276f1b14efc2c1dc8067218fade420e))


### Bug Fixes

* **client:** mark some request bodies as optional ([a4b3083](https://github.com/OneBusAway/python-sdk/commit/a4b3083b2276f1b14efc2c1dc8067218fade420e))

## 1.7.1 (2025-02-14)

Full Changelog: [v1.7.0...v1.7.1](https://github.com/OneBusAway/python-sdk/compare/v1.7.0...v1.7.1)

### Bug Fixes

* asyncify on non-asyncio runtimes ([#261](https://github.com/OneBusAway/python-sdk/issues/261)) ([5d5e531](https://github.com/OneBusAway/python-sdk/commit/5d5e5310af6acf2accc87d2d3479bbaf4f90d6e0))

## 1.7.0 (2025-02-08)

Full Changelog: [v1.6.0...v1.7.0](https://github.com/OneBusAway/python-sdk/compare/v1.6.0...v1.7.0)

### Features

* chore(tests): formatting ([dbb3cd7](https://github.com/OneBusAway/python-sdk/commit/dbb3cd78e5059a2e34efe2b323376abe7e544ac9))

## 1.6.0 (2025-02-08)

Full Changelog: [v1.5.2...v1.6.0](https://github.com/OneBusAway/python-sdk/compare/v1.5.2...v1.6.0)

### Features

* fix(tests): use urllib.parse.quote_plus for API key encoding in expected URLs ([41dfd84](https://github.com/OneBusAway/python-sdk/commit/41dfd84d5c705825fa4b0dea4d52b964b08921d0))

## 1.5.2 (2025-02-07)

Full Changelog: [v1.5.1...v1.5.2](https://github.com/OneBusAway/python-sdk/compare/v1.5.1...v1.5.2)

### Chores

* **internal:** minor type handling changes ([#254](https://github.com/OneBusAway/python-sdk/issues/254)) ([401146a](https://github.com/OneBusAway/python-sdk/commit/401146a94806dba8c0aa14252aadd09089c590b9))

## 1.5.1 (2025-02-07)

Full Changelog: [v1.5.0...v1.5.1](https://github.com/OneBusAway/python-sdk/compare/v1.5.0...v1.5.1)

### Chores

* **internal:** fix type traversing dictionary params ([#251](https://github.com/OneBusAway/python-sdk/issues/251)) ([6dc1d57](https://github.com/OneBusAway/python-sdk/commit/6dc1d570d4fa8f1391755af3431ae2cdda088d9e))

## 1.5.0 (2025-02-06)

Full Changelog: [v1.4.23...v1.5.0](https://github.com/OneBusAway/python-sdk/compare/v1.4.23...v1.5.0)

### Features

* **client:** send `X-Stainless-Read-Timeout` header ([#248](https://github.com/OneBusAway/python-sdk/issues/248)) ([2bdb366](https://github.com/OneBusAway/python-sdk/commit/2bdb366dbde6c2c9ad5e5cd89cf07b24410ca472))

## 1.4.23 (2025-02-04)

Full Changelog: [v1.4.22...v1.4.23](https://github.com/OneBusAway/python-sdk/compare/v1.4.22...v1.4.23)

### Chores

* **internal:** bummp ruff dependency ([#245](https://github.com/OneBusAway/python-sdk/issues/245)) ([b8d6007](https://github.com/OneBusAway/python-sdk/commit/b8d6007b83f20484c4172901a262414247712972))

## 1.4.22 (2025-02-04)

Full Changelog: [v1.4.21...v1.4.22](https://github.com/OneBusAway/python-sdk/compare/v1.4.21...v1.4.22)

### Chores

* **internal:** change default timeout to an int ([#242](https://github.com/OneBusAway/python-sdk/issues/242)) ([7a6abd4](https://github.com/OneBusAway/python-sdk/commit/7a6abd4930719c6451e3701f745f028999bf00b0))

## 1.4.21 (2025-01-24)

Full Changelog: [v1.4.20...v1.4.21](https://github.com/OneBusAway/python-sdk/compare/v1.4.20...v1.4.21)

### Chores

* **internal:** minor formatting changes ([#239](https://github.com/OneBusAway/python-sdk/issues/239)) ([c4753be](https://github.com/OneBusAway/python-sdk/commit/c4753be98ddcd9ef1821bf155715366a13de4542))

## 1.4.20 (2025-01-23)

Full Changelog: [v1.4.19...v1.4.20](https://github.com/OneBusAway/python-sdk/compare/v1.4.19...v1.4.20)

### Chores

* **internal:** codegen related update ([#236](https://github.com/OneBusAway/python-sdk/issues/236)) ([efffa87](https://github.com/OneBusAway/python-sdk/commit/efffa87da71fe633d206c9816f6ee79ecd564276))

## 1.4.19 (2025-01-22)

Full Changelog: [v1.4.18...v1.4.19](https://github.com/OneBusAway/python-sdk/compare/v1.4.18...v1.4.19)

### Chores

* **internal:** codegen related update ([#233](https://github.com/OneBusAway/python-sdk/issues/233)) ([2ee9813](https://github.com/OneBusAway/python-sdk/commit/2ee9813f5d3b4a4f3036f2cce685f1e2c4adaa71))

## 1.4.18 (2025-01-21)

Full Changelog: [v1.4.17...v1.4.18](https://github.com/OneBusAway/python-sdk/compare/v1.4.17...v1.4.18)

### Documentation

* **raw responses:** fix duplicate `the` ([#229](https://github.com/OneBusAway/python-sdk/issues/229)) ([3eb85fa](https://github.com/OneBusAway/python-sdk/commit/3eb85fa39efc772ba9175c5a281e19c2e22b62d4))

## 1.4.17 (2025-01-17)

Full Changelog: [v1.4.16...v1.4.17](https://github.com/OneBusAway/python-sdk/compare/v1.4.16...v1.4.17)

### Chores

* **internal:** codegen related update ([#226](https://github.com/OneBusAway/python-sdk/issues/226)) ([69f99d3](https://github.com/OneBusAway/python-sdk/commit/69f99d32d95b5256685d68874c73b2647cc8e900))

## 1.4.16 (2025-01-10)

Full Changelog: [v1.4.15...v1.4.16](https://github.com/OneBusAway/python-sdk/compare/v1.4.15...v1.4.16)

### Bug Fixes

* correctly handle deserialising `cls` fields ([#223](https://github.com/OneBusAway/python-sdk/issues/223)) ([33d5ab7](https://github.com/OneBusAway/python-sdk/commit/33d5ab7fc1366619e6db0a2ab30390ee3249bf52))

## 1.4.15 (2025-01-09)

Full Changelog: [v1.4.14...v1.4.15](https://github.com/OneBusAway/python-sdk/compare/v1.4.14...v1.4.15)

### Chores

* **internal:** codegen related update ([#220](https://github.com/OneBusAway/python-sdk/issues/220)) ([d78e83a](https://github.com/OneBusAway/python-sdk/commit/d78e83aea265d25d3a37e2fc0c1ec3aa8ea3c9f5))

## 1.4.14 (2025-01-09)

Full Changelog: [v1.4.13...v1.4.14](https://github.com/OneBusAway/python-sdk/compare/v1.4.13...v1.4.14)

### Documentation

* fix typos ([#218](https://github.com/OneBusAway/python-sdk/issues/218)) ([b66f7dd](https://github.com/OneBusAway/python-sdk/commit/b66f7dd5482920dfb986bd3e6c09c62b3fdfafb3))

## 1.4.13 (2025-01-08)

Full Changelog: [v1.4.12...v1.4.13](https://github.com/OneBusAway/python-sdk/compare/v1.4.12...v1.4.13)

### Chores

* **internal:** codegen related update ([#215](https://github.com/OneBusAway/python-sdk/issues/215)) ([f3ecad9](https://github.com/OneBusAway/python-sdk/commit/f3ecad9cbd05c928200b9ee53c2a3a0615f99822))

## 1.4.12 (2025-01-07)

Full Changelog: [v1.4.11...v1.4.12](https://github.com/OneBusAway/python-sdk/compare/v1.4.11...v1.4.12)

### Chores

* add missing isclass check ([#212](https://github.com/OneBusAway/python-sdk/issues/212)) ([989d621](https://github.com/OneBusAway/python-sdk/commit/989d6218de97f5515ec741b5cc424cb8d7901362))

## 1.4.11 (2025-01-02)

Full Changelog: [v1.4.10...v1.4.11](https://github.com/OneBusAway/python-sdk/compare/v1.4.10...v1.4.11)

### Chores

* **internal:** codegen related update ([#209](https://github.com/OneBusAway/python-sdk/issues/209)) ([922f218](https://github.com/OneBusAway/python-sdk/commit/922f218506637cff878bdd44b64a886323371ea2))

## 1.4.10 (2024-12-21)

Full Changelog: [v1.4.9...v1.4.10](https://github.com/OneBusAway/python-sdk/compare/v1.4.9...v1.4.10)

### Chores

* **internal:** fix some typos ([#205](https://github.com/OneBusAway/python-sdk/issues/205)) ([c539ec3](https://github.com/OneBusAway/python-sdk/commit/c539ec33bb73497f8f16ec7b5868f761cd0c3cb6))

## 1.4.9 (2024-12-17)

Full Changelog: [v1.4.8...v1.4.9](https://github.com/OneBusAway/python-sdk/compare/v1.4.8...v1.4.9)

### Chores

* **internal:** codegen related update ([#201](https://github.com/OneBusAway/python-sdk/issues/201)) ([a8bf61b](https://github.com/OneBusAway/python-sdk/commit/a8bf61bad113e964dd82013827ae3e3968a41527))

## 1.4.8 (2024-12-17)

Full Changelog: [v1.4.7...v1.4.8](https://github.com/OneBusAway/python-sdk/compare/v1.4.7...v1.4.8)

### Chores

* **internal:** codegen related update ([#198](https://github.com/OneBusAway/python-sdk/issues/198)) ([2210e02](https://github.com/OneBusAway/python-sdk/commit/2210e02b9e700135b282629389534a2ec064ef0d))

## 1.4.7 (2024-12-17)

Full Changelog: [v1.4.6...v1.4.7](https://github.com/OneBusAway/python-sdk/compare/v1.4.6...v1.4.7)

### Chores

* **internal:** codegen related update ([#197](https://github.com/OneBusAway/python-sdk/issues/197)) ([12f69d6](https://github.com/OneBusAway/python-sdk/commit/12f69d6a786450bdb2c8588775ba05709b61de79))

## 1.4.6 (2024-12-14)

Full Changelog: [v1.4.5...v1.4.6](https://github.com/OneBusAway/python-sdk/compare/v1.4.5...v1.4.6)

### Chores

* **internal:** codegen related update ([#194](https://github.com/OneBusAway/python-sdk/issues/194)) ([7e10c0d](https://github.com/OneBusAway/python-sdk/commit/7e10c0d81a717032bc6f10ff61ea49c6057f5610))

## 1.4.5 (2024-12-13)

Full Changelog: [v1.4.4...v1.4.5](https://github.com/OneBusAway/python-sdk/compare/v1.4.4...v1.4.5)

### Chores

* **internal:** codegen related update ([#191](https://github.com/OneBusAway/python-sdk/issues/191)) ([7bd6b7d](https://github.com/OneBusAway/python-sdk/commit/7bd6b7dd25b58fcc1e995086a380975f25535065))

## 1.4.4 (2024-12-10)

Full Changelog: [v1.4.3...v1.4.4](https://github.com/OneBusAway/python-sdk/compare/v1.4.3...v1.4.4)

### Chores

* **internal:** codegen related update ([#188](https://github.com/OneBusAway/python-sdk/issues/188)) ([6a5ace1](https://github.com/OneBusAway/python-sdk/commit/6a5ace19835fb7d3ebe9dc8c29883b5002b9967a))

## 1.4.3 (2024-12-10)

Full Changelog: [v1.4.2...v1.4.3](https://github.com/OneBusAway/python-sdk/compare/v1.4.2...v1.4.3)

### Chores

* **internal:** bump pydantic dependency ([#185](https://github.com/OneBusAway/python-sdk/issues/185)) ([592e261](https://github.com/OneBusAway/python-sdk/commit/592e2619ae0d6b486c14c25812f7e0c5402fe068))

## 1.4.2 (2024-12-04)

Full Changelog: [v1.4.1...v1.4.2](https://github.com/OneBusAway/python-sdk/compare/v1.4.1...v1.4.2)

### Chores

* make the `Omit` type public ([#182](https://github.com/OneBusAway/python-sdk/issues/182)) ([cd0f27e](https://github.com/OneBusAway/python-sdk/commit/cd0f27e796d255cf20b23b6418c200faec5b35d0))

## 1.4.1 (2024-12-03)

Full Changelog: [v1.4.0...v1.4.1](https://github.com/OneBusAway/python-sdk/compare/v1.4.0...v1.4.1)

### Chores

* **internal:** codegen related update ([#179](https://github.com/OneBusAway/python-sdk/issues/179)) ([113387e](https://github.com/OneBusAway/python-sdk/commit/113387ece3ec8ba6cfa09f9097c083e8858a7a2c))

## 1.4.0 (2024-11-29)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/OneBusAway/python-sdk/compare/v1.3.0...v1.4.0)

### Features

* **api:** api update ([#176](https://github.com/OneBusAway/python-sdk/issues/176)) ([b66eab7](https://github.com/OneBusAway/python-sdk/commit/b66eab729a4ace0919b928169f793e5ffdb62a47))

## 1.3.0 (2024-11-29)

Full Changelog: [v1.2.13...v1.3.0](https://github.com/OneBusAway/python-sdk/compare/v1.2.13...v1.3.0)

### Features

* **api:** api update ([#173](https://github.com/OneBusAway/python-sdk/issues/173)) ([91ac1e7](https://github.com/OneBusAway/python-sdk/commit/91ac1e776ed5f17d523bb61ec78d9aa9f037c5c4))

## 1.2.13 (2024-11-28)

Full Changelog: [v1.2.12...v1.2.13](https://github.com/OneBusAway/python-sdk/compare/v1.2.12...v1.2.13)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#170](https://github.com/OneBusAway/python-sdk/issues/170)) ([0409197](https://github.com/OneBusAway/python-sdk/commit/0409197d1a693e5882a4553bb5ce223c12d42966))

## 1.2.12 (2024-11-28)

Full Changelog: [v1.2.11...v1.2.12](https://github.com/OneBusAway/python-sdk/compare/v1.2.11...v1.2.12)

### Chores

* **internal:** exclude mypy from running on tests ([#167](https://github.com/OneBusAway/python-sdk/issues/167)) ([e5a89a4](https://github.com/OneBusAway/python-sdk/commit/e5a89a4ded2e8cedee272429a77c6edd921bc55d))

## 1.2.11 (2024-11-26)

Full Changelog: [v1.2.10...v1.2.11](https://github.com/OneBusAway/python-sdk/compare/v1.2.10...v1.2.11)

### Chores

* remove now unused `cached-property` dep ([#164](https://github.com/OneBusAway/python-sdk/issues/164)) ([327cdeb](https://github.com/OneBusAway/python-sdk/commit/327cdeb051074bbdb55fe9848c714e46d4c0f22b))

## 1.2.10 (2024-11-22)

Full Changelog: [v1.2.9...v1.2.10](https://github.com/OneBusAway/python-sdk/compare/v1.2.9...v1.2.10)

### Documentation

* add info log level to readme ([#161](https://github.com/OneBusAway/python-sdk/issues/161)) ([4b74a14](https://github.com/OneBusAway/python-sdk/commit/4b74a1477b8492d102775395bd688fb2cefd17fa))

## 1.2.9 (2024-11-22)

Full Changelog: [v1.2.8...v1.2.9](https://github.com/OneBusAway/python-sdk/compare/v1.2.8...v1.2.9)

### Chores

* **internal:** fix compat model_dump method when warnings are passed ([#158](https://github.com/OneBusAway/python-sdk/issues/158)) ([699d488](https://github.com/OneBusAway/python-sdk/commit/699d4889cf96d12c9fc0c538e228daaab97084be))

## 1.2.8 (2024-11-18)

Full Changelog: [v1.2.7...v1.2.8](https://github.com/OneBusAway/python-sdk/compare/v1.2.7...v1.2.8)

### Chores

* rebuild project due to codegen change ([#155](https://github.com/OneBusAway/python-sdk/issues/155)) ([a1206f8](https://github.com/OneBusAway/python-sdk/commit/a1206f8cc69bef31c4932b8160bdb64a1458597d))

## 1.2.7 (2024-11-12)

Full Changelog: [v1.2.6...v1.2.7](https://github.com/OneBusAway/python-sdk/compare/v1.2.6...v1.2.7)

### Chores

* rebuild project due to codegen change ([#152](https://github.com/OneBusAway/python-sdk/issues/152)) ([0ccfcf3](https://github.com/OneBusAway/python-sdk/commit/0ccfcf34a65fe87d1b226598585022c305ffc41f))

## 1.2.6 (2024-11-12)

Full Changelog: [v1.2.5...v1.2.6](https://github.com/OneBusAway/python-sdk/compare/v1.2.5...v1.2.6)

### Chores

* rebuild project due to codegen change ([#149](https://github.com/OneBusAway/python-sdk/issues/149)) ([a4f5f5c](https://github.com/OneBusAway/python-sdk/commit/a4f5f5c8374fd0882ec00d8fbd79d1ddb8ecf684))

## 1.2.5 (2024-11-06)

Full Changelog: [v1.2.4...v1.2.5](https://github.com/OneBusAway/python-sdk/compare/v1.2.4...v1.2.5)

### Chores

* rebuild project due to codegen change ([#144](https://github.com/OneBusAway/python-sdk/issues/144)) ([8a06a1e](https://github.com/OneBusAway/python-sdk/commit/8a06a1eb978f762a36d17dc9ff83fbc8a13493a8))
* rebuild project due to codegen change ([#146](https://github.com/OneBusAway/python-sdk/issues/146)) ([2dcaaff](https://github.com/OneBusAway/python-sdk/commit/2dcaaffbd9de815c6a1b26091e142c1f94bb5e4e))

## 1.2.4 (2024-11-04)

Full Changelog: [v1.2.3...v1.2.4](https://github.com/OneBusAway/python-sdk/compare/v1.2.3...v1.2.4)

### Chores

* rebuild project due to codegen change ([#141](https://github.com/OneBusAway/python-sdk/issues/141)) ([d52c16a](https://github.com/OneBusAway/python-sdk/commit/d52c16af30fdfb61b324c5d83f4052726f2eacd8))

## 1.2.3 (2024-11-02)

Full Changelog: [v1.2.2...v1.2.3](https://github.com/OneBusAway/python-sdk/compare/v1.2.2...v1.2.3)

### Chores

* rebuild project due to codegen change ([#138](https://github.com/OneBusAway/python-sdk/issues/138)) ([2b313bd](https://github.com/OneBusAway/python-sdk/commit/2b313bd9f439d8e908a79b5f498e490ce68a06fe))

## 1.2.2 (2024-11-01)

Full Changelog: [v1.2.1...v1.2.2](https://github.com/OneBusAway/python-sdk/compare/v1.2.1...v1.2.2)

### Chores

* rebuild project due to codegen change ([#135](https://github.com/OneBusAway/python-sdk/issues/135)) ([34f0283](https://github.com/OneBusAway/python-sdk/commit/34f02834030b10d71061287edcdfe7104f5fccbd))

## 1.2.1 (2024-10-28)

Full Changelog: [v1.2.0...v1.2.1](https://github.com/OneBusAway/python-sdk/compare/v1.2.0...v1.2.1)

### Chores

* rebuild project due to codegen change ([#132](https://github.com/OneBusAway/python-sdk/issues/132)) ([39da39b](https://github.com/OneBusAway/python-sdk/commit/39da39bb4d2e0e644a66a24b199f7b4e506c46fd))

## 1.2.0 (2024-10-22)

Full Changelog: [v1.1.6...v1.2.0](https://github.com/OneBusAway/python-sdk/compare/v1.1.6...v1.2.0)

### Features

* **api:** api update ([#129](https://github.com/OneBusAway/python-sdk/issues/129)) ([fa000a7](https://github.com/OneBusAway/python-sdk/commit/fa000a7c52befc4916757055e2019174bba553f5))

## 1.1.6 (2024-10-07)

Full Changelog: [v1.1.5...v1.1.6](https://github.com/OneBusAway/python-sdk/compare/v1.1.5...v1.1.6)

### Chores

* add repr to PageInfo class ([#126](https://github.com/OneBusAway/python-sdk/issues/126)) ([4904f20](https://github.com/OneBusAway/python-sdk/commit/4904f2016d302d002f08455737f8a76c5784980e))

## 1.1.5 (2024-10-07)

Full Changelog: [v1.1.4...v1.1.5](https://github.com/OneBusAway/python-sdk/compare/v1.1.4...v1.1.5)

### Bug Fixes

* **client:** avoid OverflowError with very large retry counts ([#124](https://github.com/OneBusAway/python-sdk/issues/124)) ([5f67626](https://github.com/OneBusAway/python-sdk/commit/5f6762604b6462d1fbac9b72adba324d2e4cc38d))

## 1.1.4 (2024-10-07)

Full Changelog: [v1.1.3...v1.1.4](https://github.com/OneBusAway/python-sdk/compare/v1.1.3...v1.1.4)

### Chores

* **internal:** add support for parsing bool response content ([#121](https://github.com/OneBusAway/python-sdk/issues/121)) ([390f17a](https://github.com/OneBusAway/python-sdk/commit/390f17a0a9ca9da54dac53982bfd72fa851191ff))

## 1.1.3 (2024-10-02)

Full Changelog: [v1.1.2...v1.1.3](https://github.com/OneBusAway/python-sdk/compare/v1.1.2...v1.1.3)

### Chores

* **internal:** codegen related update ([#116](https://github.com/OneBusAway/python-sdk/issues/116)) ([2f6a75e](https://github.com/OneBusAway/python-sdk/commit/2f6a75ec99dd716f9bdf2a496e8539c523845501))

## 1.1.2 (2024-10-02)

Full Changelog: [v1.1.1...v1.1.2](https://github.com/OneBusAway/python-sdk/compare/v1.1.1...v1.1.2)

### Chores

* **internal:** codegen related update ([#115](https://github.com/OneBusAway/python-sdk/issues/115)) ([ca402ef](https://github.com/OneBusAway/python-sdk/commit/ca402ef31d5bdba075c4a2888ab72905e14dc2cc))

## 1.1.1 (2024-09-27)

Full Changelog: [v1.1.0...v1.1.1](https://github.com/OneBusAway/python-sdk/compare/v1.1.0...v1.1.1)

### Chores

* **internal:** codegen related update ([#112](https://github.com/OneBusAway/python-sdk/issues/112)) ([646ad67](https://github.com/OneBusAway/python-sdk/commit/646ad67c30929ccb7bc40e6667a93712284c3c30))

## 1.1.0 (2024-09-11)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/OneBusAway/python-sdk/compare/v1.0.0...v1.1.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#110](https://github.com/OneBusAway/python-sdk/issues/110)) ([6ae5ddf](https://github.com/OneBusAway/python-sdk/commit/6ae5ddf666032f4374abf719b02127326c8b344f))


### Chores

* add docstrings to raw response properties ([#107](https://github.com/OneBusAway/python-sdk/issues/107)) ([0fecff5](https://github.com/OneBusAway/python-sdk/commit/0fecff5be41b8bc6049a49ed56eb80399eccf775))
* **internal:** codegen related update ([#105](https://github.com/OneBusAway/python-sdk/issues/105)) ([1c46884](https://github.com/OneBusAway/python-sdk/commit/1c46884dffc5766e2c0b03826b341e658ef4b58b))
* **internal:** codegen related update ([#109](https://github.com/OneBusAway/python-sdk/issues/109)) ([89d809e](https://github.com/OneBusAway/python-sdk/commit/89d809e01baa6cd1b1b98c45e88853584f8ac8a3))


### Documentation

* **readme:** add section on determining installed version ([#108](https://github.com/OneBusAway/python-sdk/issues/108)) ([01b74e9](https://github.com/OneBusAway/python-sdk/commit/01b74e91f822fedd4407b5de3d2fca1d03aaecbb))

## 1.0.0 (2024-08-28)

Full Changelog: [v0.1.0-alpha.19...v1.0.0](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.19...v1.0.0)

### Chores

* release: 1.0.0 ([709a130](https://github.com/OneBusAway/python-sdk/commit/709a1305f5dfd8aed9f95ee69ffd0f192c1b413e))

## 0.1.0-alpha.19 (2024-08-24)

Full Changelog: [v0.1.0-alpha.18...v0.1.0-alpha.19](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.18...v0.1.0-alpha.19)

### Features

* **api:** OpenAPI spec update via Stainless API ([#99](https://github.com/OneBusAway/python-sdk/issues/99)) ([e2d03b3](https://github.com/OneBusAway/python-sdk/commit/e2d03b34d459ca5954c40af72c0a8ec13ca19f7e))

## 0.1.0-alpha.18 (2024-08-20)

Full Changelog: [v0.1.0-alpha.17...v0.1.0-alpha.18](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.17...v0.1.0-alpha.18)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#81](https://github.com/OneBusAway/python-sdk/issues/81)) ([71f8ac8](https://github.com/OneBusAway/python-sdk/commit/71f8ac8808bc984dc772435e3dd25fb851a27156))
-   **api:** OpenAPI spec update via Stainless API ([#85](https://github.com/OneBusAway/python-sdk/issues/85)) ([87a9f3f](https://github.com/OneBusAway/python-sdk/commit/87a9f3fe8cecfc7c527ab99cd98fcd93d5a62084))
-   **api:** OpenAPI spec update via Stainless API ([#86](https://github.com/OneBusAway/python-sdk/issues/86)) ([d63524a](https://github.com/OneBusAway/python-sdk/commit/d63524a8e1e7a3ab863e964f2f81069fdd4e5761))
-   **api:** OpenAPI spec update via Stainless API ([#87](https://github.com/OneBusAway/python-sdk/issues/87)) ([d4f2ca0](https://github.com/OneBusAway/python-sdk/commit/d4f2ca03ce7778c127e70a6f7db86e0fb667e157))
-   **api:** OpenAPI spec update via Stainless API ([#88](https://github.com/OneBusAway/python-sdk/issues/88)) ([3543b38](https://github.com/OneBusAway/python-sdk/commit/3543b38cf9e4b8a4762c41f494c8f54a6451d091))
-   **api:** OpenAPI spec update via Stainless API ([#89](https://github.com/OneBusAway/python-sdk/issues/89)) ([b56865a](https://github.com/OneBusAway/python-sdk/commit/b56865a9f16ef4117ac278dec6174a3507b4b1dc))
-   **api:** OpenAPI spec update via Stainless API ([#93](https://github.com/OneBusAway/python-sdk/issues/93)) ([be44ac5](https://github.com/OneBusAway/python-sdk/commit/be44ac517f04b963fc27b68d07f94b7da9fb7380))
-   **api:** OpenAPI spec update via Stainless API ([#94](https://github.com/OneBusAway/python-sdk/issues/94)) ([2ebd77c](https://github.com/OneBusAway/python-sdk/commit/2ebd77c7d359fd48b7ed8104223db7abc0157de1))
-   **api:** OpenAPI spec update via Stainless API ([#95](https://github.com/OneBusAway/python-sdk/issues/95)) ([54d58cf](https://github.com/OneBusAway/python-sdk/commit/54d58cf81718aee18e852dda9ad260dfa9392404))
-   **api:** OpenAPI spec update via Stainless API ([#96](https://github.com/OneBusAway/python-sdk/issues/96)) ([7cc92e8](https://github.com/OneBusAway/python-sdk/commit/7cc92e8d051f011599844cd9d3851521a94cc49b))
-   **api:** OpenAPI spec update via Stainless API ([#97](https://github.com/OneBusAway/python-sdk/issues/97)) ([c3ca610](https://github.com/OneBusAway/python-sdk/commit/c3ca610df71affbe1381fcfa5a85f22614098beb))

### Chores

-   **ci:** also run pydantic v1 tests ([#92](https://github.com/OneBusAway/python-sdk/issues/92)) ([19a0334](https://github.com/OneBusAway/python-sdk/commit/19a03345944154c4db06c96304e2e9b5bb2cbc57))
-   **client:** fix parsing union responses when non-json is returned ([#91](https://github.com/OneBusAway/python-sdk/issues/91)) ([38860c1](https://github.com/OneBusAway/python-sdk/commit/38860c19de2e79ab7ca5054c2ec9357a1fd3690b))
-   **internal:** codegen related update ([#83](https://github.com/OneBusAway/python-sdk/issues/83)) ([bb39847](https://github.com/OneBusAway/python-sdk/commit/bb398472831ec5623b587568acfd99ecd44be886))
-   **internal:** use different 32bit detection method ([#84](https://github.com/OneBusAway/python-sdk/issues/84)) ([8dbeb49](https://github.com/OneBusAway/python-sdk/commit/8dbeb49a6f799aaef5214d77cfa46ae0d45fd635))

## 0.1.0-alpha.17 (2024-08-12)

Full Changelog: [v0.1.0-alpha.16...v0.1.0-alpha.17](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.16...v0.1.0-alpha.17)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#77](https://github.com/OneBusAway/python-sdk/issues/77)) ([70ce97c](https://github.com/OneBusAway/python-sdk/commit/70ce97c2c90dcfa6635fd36f83a7fb71a321ca69))
-   **api:** update via SDK Studio ([#79](https://github.com/OneBusAway/python-sdk/issues/79)) ([b31341a](https://github.com/OneBusAway/python-sdk/commit/b31341a157b8b9aa554ad161afcbc581a041c3fb))

## 0.1.0-alpha.16 (2024-08-10)

Full Changelog: [v0.1.0-alpha.15...v0.1.0-alpha.16](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.15...v0.1.0-alpha.16)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#71](https://github.com/OneBusAway/python-sdk/issues/71)) ([876b77c](https://github.com/OneBusAway/python-sdk/commit/876b77c3addf2460c3116738f7b4bc784f67350d))
-   **api:** OpenAPI spec update via Stainless API ([#75](https://github.com/OneBusAway/python-sdk/issues/75)) ([6af5d8a](https://github.com/OneBusAway/python-sdk/commit/6af5d8a93d7f516c9bb7a20e20d063944d0435e9))

### Chores

-   **ci:** bump prism mock server version ([#73](https://github.com/OneBusAway/python-sdk/issues/73)) ([e303bb6](https://github.com/OneBusAway/python-sdk/commit/e303bb64a39d45801d72141e13e00bac40771f71))
-   **internal:** ensure package is importable in lint cmd ([#74](https://github.com/OneBusAway/python-sdk/issues/74)) ([b4db5b9](https://github.com/OneBusAway/python-sdk/commit/b4db5b955b4880c1eea3bba00749bb9f4a78416b))

## 0.1.0-alpha.15 (2024-08-08)

Full Changelog: [v0.1.0-alpha.14...v0.1.0-alpha.15](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.14...v0.1.0-alpha.15)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#68](https://github.com/OneBusAway/python-sdk/issues/68)) ([6367613](https://github.com/OneBusAway/python-sdk/commit/63676136b6d0b0f01738cfc778763b6a79775d09))

## 0.1.0-alpha.14 (2024-08-08)

Full Changelog: [v0.1.0-alpha.13...v0.1.0-alpha.14](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.13...v0.1.0-alpha.14)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#65](https://github.com/OneBusAway/python-sdk/issues/65)) ([d93e82a](https://github.com/OneBusAway/python-sdk/commit/d93e82a4b6410768f1d5f9cd08ee83157eb405ce))

## 0.1.0-alpha.13 (2024-08-08)

Full Changelog: [v0.1.0-alpha.12...v0.1.0-alpha.13](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.12...v0.1.0-alpha.13)

### Chores

-   **internal:** version bump ([#61](https://github.com/OneBusAway/python-sdk/issues/61)) ([5d7fe06](https://github.com/OneBusAway/python-sdk/commit/5d7fe060b6158f719e388feba0bc9f7dcb0fe288))

## 0.1.0-alpha.12 (2024-08-08)

Full Changelog: [v0.1.0-alpha.11...v0.1.0-alpha.12](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.11...v0.1.0-alpha.12)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#48](https://github.com/OneBusAway/python-sdk/issues/48)) ([a5c305c](https://github.com/OneBusAway/python-sdk/commit/a5c305c7a5614588dd3fb14607dd2489aab8b3c6))
-   **api:** OpenAPI spec update via Stainless API ([#55](https://github.com/OneBusAway/python-sdk/issues/55)) ([9adae4d](https://github.com/OneBusAway/python-sdk/commit/9adae4de96b8ea11ff8e2d7c251183580f86cf8a))
-   **api:** OpenAPI spec update via Stainless API ([#56](https://github.com/OneBusAway/python-sdk/issues/56)) ([1882cdc](https://github.com/OneBusAway/python-sdk/commit/1882cdc8a4da9705c853ed6f5d5e8d73a4b9276c))
-   **api:** OpenAPI spec update via Stainless API ([#57](https://github.com/OneBusAway/python-sdk/issues/57)) ([5c8a7ee](https://github.com/OneBusAway/python-sdk/commit/5c8a7ee00dcd4ab6a3a9b6800fe10f7447d79c61))
-   **api:** OpenAPI spec update via Stainless API ([#58](https://github.com/OneBusAway/python-sdk/issues/58)) ([29edb45](https://github.com/OneBusAway/python-sdk/commit/29edb45798ad111a1a4f6ce5bbbbadfe3e9099d8))
-   **client:** add `retry_count` to raw response class ([#51](https://github.com/OneBusAway/python-sdk/issues/51)) ([97156e5](https://github.com/OneBusAway/python-sdk/commit/97156e5dff5d743d04ecc0dbe73ec7c690dfb4fe))

### Chores

-   **internal:** bump pyright ([#50](https://github.com/OneBusAway/python-sdk/issues/50)) ([6d1fdf7](https://github.com/OneBusAway/python-sdk/commit/6d1fdf78cf6d63079bf037b88ac0540e619f9ae7))
-   **internal:** bump ruff version ([#53](https://github.com/OneBusAway/python-sdk/issues/53)) ([c8cbc6a](https://github.com/OneBusAway/python-sdk/commit/c8cbc6a1e48e42b15e42ebf40cdfd2f8fc0bc7ab))
-   **internal:** remove deprecated ruff config ([#59](https://github.com/OneBusAway/python-sdk/issues/59)) ([a6413af](https://github.com/OneBusAway/python-sdk/commit/a6413af808c1ea04d05a46fa0a5d54ec888999bf))
-   **internal:** test updates ([#52](https://github.com/OneBusAway/python-sdk/issues/52)) ([f3b7cb0](https://github.com/OneBusAway/python-sdk/commit/f3b7cb00c4302b0ac1b8497835f2db0d3f9e7949))
-   **internal:** update pydantic compat helper function ([#54](https://github.com/OneBusAway/python-sdk/issues/54)) ([1f501f0](https://github.com/OneBusAway/python-sdk/commit/1f501f0592c92e86c4c027f652a49ff11a068715))

## 0.1.0-alpha.11 (2024-08-01)

Full Changelog: [v0.1.0-alpha.10...v0.1.0-alpha.11](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.10...v0.1.0-alpha.11)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#43](https://github.com/OneBusAway/python-sdk/issues/43)) ([d80d795](https://github.com/OneBusAway/python-sdk/commit/d80d795cf0dfce32a27986630065fcf3f93a0eaa))
-   **api:** OpenAPI spec update via Stainless API ([#44](https://github.com/OneBusAway/python-sdk/issues/44)) ([c79102d](https://github.com/OneBusAway/python-sdk/commit/c79102d2c079e23c77dd4583485b967cf8eaddc1))
-   **api:** OpenAPI spec update via Stainless API ([#45](https://github.com/OneBusAway/python-sdk/issues/45)) ([138c1c3](https://github.com/OneBusAway/python-sdk/commit/138c1c35902a68e251796e4713fcfeb609fb2592))
-   chore: Refactor code by removing unnecessary blank lines ([9dfffd8](https://github.com/OneBusAway/python-sdk/commit/9dfffd881f9bbe738a2af883ef1dae8db68c7eb7))
-   various codegen changes ([1cba822](https://github.com/OneBusAway/python-sdk/commit/1cba822390c0a6e2c2d8f3f9e101215a1abc22cc))

## 0.1.0-alpha.10 (2024-07-31)

Full Changelog: [v0.1.0-alpha.9...v0.1.0-alpha.10](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.9...v0.1.0-alpha.10)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#37](https://github.com/OneBusAway/python-sdk/issues/37)) ([cc7611d](https://github.com/OneBusAway/python-sdk/commit/cc7611d6984efe9cce70b1388c8bdfd14ed814d3))
-   **api:** OpenAPI spec update via Stainless API ([#39](https://github.com/OneBusAway/python-sdk/issues/39)) ([45dc9fe](https://github.com/OneBusAway/python-sdk/commit/45dc9fe6b89ab5224d6f60d97d10ab85326e08fd))

## 0.1.0-alpha.9 (2024-07-31)

Full Changelog: [v0.1.0-alpha.8...v0.1.0-alpha.9](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.8...v0.1.0-alpha.9)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#34](https://github.com/OneBusAway/python-sdk/issues/34)) ([d60f5d7](https://github.com/OneBusAway/python-sdk/commit/d60f5d72bed809667875d4548bc4909d5125a6d5))

## 0.1.0-alpha.8 (2024-07-30)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#31](https://github.com/OneBusAway/python-sdk/issues/31)) ([891cdf5](https://github.com/OneBusAway/python-sdk/commit/891cdf59961594e7bfb21fc25e8615b3c536dc8e))

## 0.1.0-alpha.7 (2024-07-29)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Chores

-   **internal:** add type construction helper ([#27](https://github.com/OneBusAway/python-sdk/issues/27)) ([ceb8e94](https://github.com/OneBusAway/python-sdk/commit/ceb8e94522516242dc400c281133c053ddcc7961))

## 0.1.0-alpha.6 (2024-07-29)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#22](https://github.com/OneBusAway/python-sdk/issues/22)) ([54e9f2a](https://github.com/OneBusAway/python-sdk/commit/54e9f2aefaf7a88392bf23ec3301efd2191013a7))
-   **api:** OpenAPI spec update via Stainless API ([#25](https://github.com/OneBusAway/python-sdk/issues/25)) ([64e3e43](https://github.com/OneBusAway/python-sdk/commit/64e3e4396b25d8d80ddee38ec99cda8409b0f597))

### Chores

-   **internal:** add type construction helper ([#24](https://github.com/OneBusAway/python-sdk/issues/24)) ([92184d0](https://github.com/OneBusAway/python-sdk/commit/92184d0e99d1ed3b9ccc13adf5aaa7bc6ddb334b))

## 0.1.0-alpha.5 (2024-07-28)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#18](https://github.com/OneBusAway/python-sdk/issues/18)) ([e209b47](https://github.com/OneBusAway/python-sdk/commit/e209b47d717f9ad08a688587b1bae46cb71fab54))

## 0.1.0-alpha.4 (2024-07-27)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#15](https://github.com/OneBusAway/python-sdk/issues/15)) ([171d1b7](https://github.com/OneBusAway/python-sdk/commit/171d1b79ca2cc120d315566f3f861c96a05d8a3b))

## 0.1.0-alpha.3 (2024-07-27)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#10](https://github.com/OneBusAway/python-sdk/issues/10)) ([72b1a9c](https://github.com/OneBusAway/python-sdk/commit/72b1a9cead47f18491e1119a836088e20bb0d5f4))

### Chores

-   **internal:** refactor release doctor script ([#12](https://github.com/OneBusAway/python-sdk/issues/12)) ([ee1f10f](https://github.com/OneBusAway/python-sdk/commit/ee1f10fc42fbda4a4df01d58636d5b6c8209fc70))
-   **tests:** update prism version ([#13](https://github.com/OneBusAway/python-sdk/issues/13)) ([4298ff4](https://github.com/OneBusAway/python-sdk/commit/4298ff401d952e2ed17674b59001bb5d1146ae6d))

## 0.1.0-alpha.2 (2024-07-22)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/OneBusAway/python-sdk/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

-   **api:** OpenAPI spec update via Stainless API ([#4](https://github.com/OneBusAway/python-sdk/issues/4)) ([fc1679d](https://github.com/OneBusAway/python-sdk/commit/fc1679d6086747ac91152587e272d6b2b32a97fd))
-   **api:** OpenAPI spec update via Stainless API ([#6](https://github.com/OneBusAway/python-sdk/issues/6)) ([b6a54cf](https://github.com/OneBusAway/python-sdk/commit/b6a54cfdac1ecfb398e20a4efa90294bde711490))
-   **api:** OpenAPI spec update via Stainless API ([#7](https://github.com/OneBusAway/python-sdk/issues/7)) ([448c0e3](https://github.com/OneBusAway/python-sdk/commit/448c0e3847375dcdb86f9cda1e8206f64910e6e9))
-   **api:** OpenAPI spec update via Stainless API ([#8](https://github.com/OneBusAway/python-sdk/issues/8)) ([361ab73](https://github.com/OneBusAway/python-sdk/commit/361ab733efaef27d9553cabde2844ffb95296979))
-   refactor: Remove print statement from main_sync function ([b72a7a1](https://github.com/OneBusAway/python-sdk/commit/b72a7a16aaf67c5d265cb995181e1abea6d7fed2))
-   refactor: Remove print statement from main_sync function ([dcd9e3b](https://github.com/OneBusAway/python-sdk/commit/dcd9e3b609078c5fcbb9682ae4f92849bc7291cf))

## 0.1.0-alpha.1 (2024-07-14)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/OneBusAway/python-sdk/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

-   **api:** update trip resource endpoint to use trip_id parameter ([505ac28](https://github.com/OneBusAway/python-sdk/commit/505ac28c233cdc34210863decd6bce6388d299b3))
-   **api:** update via SDK Studio ([2fc0ce6](https://github.com/OneBusAway/python-sdk/commit/2fc0ce66e2d210b9d39a754dc412a1f78dde2425))
-   **api:** update via SDK Studio ([58b87fc](https://github.com/OneBusAway/python-sdk/commit/58b87fc149b3a748b56a742b1312df4b7a288dc8))
-   **api:** update via SDK Studio ([6fce548](https://github.com/OneBusAway/python-sdk/commit/6fce548afe8bd6c6cc7dfbee8cf2ae7eab4b17b6))
-   **api:** update via SDK Studio ([7586440](https://github.com/OneBusAway/python-sdk/commit/75864402b21644233224847f316a3a4ed226eaa0))
-   **api:** update via SDK Studio ([7a43139](https://github.com/OneBusAway/python-sdk/commit/7a431396cec7698593864f004ae7ae26bc48f407))
-   **api:** update via SDK Studio ([9d44ad8](https://github.com/OneBusAway/python-sdk/commit/9d44ad8bdeeed5dd3565e7382f510a7c7b6c3425))
-   **api:** update via SDK Studio ([92f3ad8](https://github.com/OneBusAway/python-sdk/commit/92f3ad86c78f8fcacb9db900bfcc6c5e1430d6d4))
-   **api:** update via SDK Studio ([6155c59](https://github.com/OneBusAway/python-sdk/commit/6155c591599e910f3c1a6c27fa410f5f95d0efc1))
-   **api:** update via SDK Studio ([c581bdb](https://github.com/OneBusAway/python-sdk/commit/c581bdb1782dba7b12e491968a2bd28aa01da6d3))
-   **api:** update via SDK Studio ([fdb908c](https://github.com/OneBusAway/python-sdk/commit/fdb908c5d0ebf12f331be0c10e7d714ece909296))
-   **api:** update via SDK Studio ([f1b0a5f](https://github.com/OneBusAway/python-sdk/commit/f1b0a5fb344842bda01724c0adb7043f8d83ba3e))
-   **api:** update via SDK Studio ([85038fe](https://github.com/OneBusAway/python-sdk/commit/85038fe848673570ccdfd95b58be840c86e306bd))
-   **api:** update via SDK Studio ([7da9927](https://github.com/OneBusAway/python-sdk/commit/7da992794551c82dfd53ec6f0a04ea745e4faf69))
-   **api:** update via SDK Studio ([9521b6e](https://github.com/OneBusAway/python-sdk/commit/9521b6e7baeae134a86abb81a67967782fe8201e))
-   **api:** update via SDK Studio ([b22b033](https://github.com/OneBusAway/python-sdk/commit/b22b0330bf195b5d23bbe56e8654cf74e8aa4b13))
-   **api:** update via SDK Studio ([f8926c3](https://github.com/OneBusAway/python-sdk/commit/f8926c35c8fc29a84ceb87acf027d5442da9a090))
-   **api:** update via SDK Studio ([0854942](https://github.com/OneBusAway/python-sdk/commit/08549428c36d5fa7e5e1db1b4095cd33e4228bff))
-   **api:** update via SDK Studio ([7ddaf77](https://github.com/OneBusAway/python-sdk/commit/7ddaf77a336bbe1f058e80dd24b3cf10832a5c26))
-   **api:** update via SDK Studio ([0809c44](https://github.com/OneBusAway/python-sdk/commit/0809c449d74a685fb8f3320c397e2ad9602ead5f))
-   **api:** update via SDK Studio ([84da952](https://github.com/OneBusAway/python-sdk/commit/84da952b7e17b6ffe6044b562bb5a8b699e33971))
-   **api:** update via SDK Studio ([db3e659](https://github.com/OneBusAway/python-sdk/commit/db3e659d827c0f782658a9ba5ea66fb1cacd057d))
-   **api:** update via SDK Studio ([3beb328](https://github.com/OneBusAway/python-sdk/commit/3beb328f733f04252725ea46b2b67588a87aa0c4))
-   **api:** update via SDK Studio ([1decfcf](https://github.com/OneBusAway/python-sdk/commit/1decfcf8e8b62d137c205bb68103130954d425e4))
-   **api:** update via SDK Studio ([0ad9c15](https://github.com/OneBusAway/python-sdk/commit/0ad9c159c08945fa8fde230d133934c319af8a21))
-   **api:** update via SDK Studio ([5ce8b85](https://github.com/OneBusAway/python-sdk/commit/5ce8b8522d5dff1435a433699d0eaa21177ed147))
-   **api:** update via SDK Studio ([1b32372](https://github.com/OneBusAway/python-sdk/commit/1b32372e013eaf55acd3fa9fbeca12e9178a9063))
-   **api:** update via SDK Studio ([ba50d73](https://github.com/OneBusAway/python-sdk/commit/ba50d73823485025802164f0a90bcda5d456f488))
-   **api:** update via SDK Studio ([295f030](https://github.com/OneBusAway/python-sdk/commit/295f030e4584f83065c340fa907ebe18c1cca1d7))
-   **api:** update via SDK Studio ([cfdc365](https://github.com/OneBusAway/python-sdk/commit/cfdc365c5711df9aea710ab40f394097be87283c))
-   **api:** update via SDK Studio ([21115c3](https://github.com/OneBusAway/python-sdk/commit/21115c3b2134638118425bf9ec4d682403519c37))
-   **api:** update via SDK Studio ([a80244d](https://github.com/OneBusAway/python-sdk/commit/a80244d027a606fdaf9df9049bb0941a2b29d1ff))
-   **api:** update via SDK Studio ([f2a3418](https://github.com/OneBusAway/python-sdk/commit/f2a34180fb1bbd73adecae83503a4417cc2dd013))
-   **api:** update via SDK Studio ([80a7f9e](https://github.com/OneBusAway/python-sdk/commit/80a7f9ede0b1ff0b4c2de938166a02136b0da2fe))
-   **api:** update via SDK Studio ([b0bab66](https://github.com/OneBusAway/python-sdk/commit/b0bab660fe8a5ae248b554be13eea215957e5f44))
-   **api:** update via SDK Studio ([fc88be6](https://github.com/OneBusAway/python-sdk/commit/fc88be647860cb3bf94d9799ed5fcd607dc2fc50))
-   **api:** update via SDK Studio ([2d32178](https://github.com/OneBusAway/python-sdk/commit/2d321788f506d3ec776ed10a3dafe315ede012a2))
-   **api:** update via SDK Studio ([4094e8a](https://github.com/OneBusAway/python-sdk/commit/4094e8acbf4ce995381c8aaf179ec03011d24a51))
-   **api:** update via SDK Studio ([#1](https://github.com/OneBusAway/python-sdk/issues/1)) ([70824e7](https://github.com/OneBusAway/python-sdk/commit/70824e7f4278cba8fe045dd749d07577a21d2887))
-   **Examples:** add agency endpoint ([c5f808a](https://github.com/OneBusAway/python-sdk/commit/c5f808a122fa2cf10651983f2e2070590fcda24e))
-   **examples:** add example for testing api response ([98d1952](https://github.com/OneBusAway/python-sdk/commit/98d1952000347909010e81cd69363e943a4e33c8))

### Chores

-   configure new SDK language ([23b3c89](https://github.com/OneBusAway/python-sdk/commit/23b3c890438d14ae70957aa275e9305dfaf49648))
-   configure new SDK language ([9a9c0c6](https://github.com/OneBusAway/python-sdk/commit/9a9c0c65509d93e2221e41a9f408d326d6e48211))
-   configure new SDK language ([63065e2](https://github.com/OneBusAway/python-sdk/commit/63065e26f68b57b0c74f457c926b38d7dcf600e7))
-   configure new SDK language ([84b1ca6](https://github.com/OneBusAway/python-sdk/commit/84b1ca654f31302265219242964ab5700ef45148))
-   configure new SDK language ([4b14ec2](https://github.com/OneBusAway/python-sdk/commit/4b14ec2cce6a83b529db5525636ffe14a0148916))
-   configure new SDK language ([267eede](https://github.com/OneBusAway/python-sdk/commit/267eeded6e0de5d709d912ee5940b03660b1c806))
-   format agency.py ([7776ddd](https://github.com/OneBusAway/python-sdk/commit/7776ddde7d1468f85d0e238537e87b6098a09e05))
-   update SDK settings ([9bf975b](https://github.com/OneBusAway/python-sdk/commit/9bf975bd37829d53c730424fe4b3956a63d4d997))
-   update SDK settings ([4886cd2](https://github.com/OneBusAway/python-sdk/commit/4886cd2bdf3a1703e907ee3a273a1be00d025ce6))

### Refactors

-   **Api:** update agency resource endpoint to use agency_id parameter ([3760fc5](https://github.com/OneBusAway/python-sdk/commit/3760fc5d6969be25dc1228af68d927cae7c41863))
-   **Api:** update API endpoint to use stop_id variable ([91625b8](https://github.com/OneBusAway/python-sdk/commit/91625b8671dd561c340e74c1d8a8ecdd8496fd7b))
-   **api:** update arrival and departure resource endpoints to use stop_id parameter ([f267a9c](https://github.com/OneBusAway/python-sdk/commit/f267a9c20647ee6c2e3b5ab0a4d87862372fdb82))
-   **api:** update tests endpoint to use api_key in param ([446cafd](https://github.com/OneBusAway/python-sdk/commit/446cafd532c627fb46c35887e4d2a32c16e5b726))
-   **client:** update auth_headers method to return an empty dictionary ([8133b61](https://github.com/OneBusAway/python-sdk/commit/8133b61a7776964d965c14276dba02d6639149e2))
-   **EndPoint:** update agency API endpoint to use agency_id variable ([6abcaa6](https://github.com/OneBusAway/python-sdk/commit/6abcaa66d066b5fb5fab379d5d26d12f4c63c806))
-   **examples:** remove commented code and unused imports ([ffe2774](https://github.com/OneBusAway/python-sdk/commit/ffe27745b20e593f2770285d122bf53128b374a0))
-   **route:** update route API endpoint to use route_id variable ([9857e55](https://github.com/OneBusAway/python-sdk/commit/9857e558f2f0ad355ca90af74978e23d48ba0948))
-   **route:** update route resource endpoint to use route_id parameter ([643d71d](https://github.com/OneBusAway/python-sdk/commit/643d71da89b6e02275b032e6bd7a78b17066f06b))
-   **test_transform:** fix base64 encoding issue ([fefa1fb](https://github.com/OneBusAway/python-sdk/commit/fefa1fb8d02dcc8c9b536f11cd3388b3ef3d8055))
-   **test_transform:** fix base64 encoding issue ([9f35949](https://github.com/OneBusAway/python-sdk/commit/9f35949d97c184fb01e3df0bcd4a41bb43b3288d))
-   **test_transform:** optimize base64 encoding ([1b2f58e](https://github.com/OneBusAway/python-sdk/commit/1b2f58e3ba3c76d13714e2b46b79ba2c7580ed29))
-   **test_transform:** update base64 encoding ([b51acbe](https://github.com/OneBusAway/python-sdk/commit/b51acbee92d24aabb3c403b8a53a13a5e2e3c9ca))
-   **test_transform:** update base64 encoding ([62ba4f2](https://github.com/OneBusAway/python-sdk/commit/62ba4f2ddcdb96a030d7b2ca7300b9ea3c35f504))
-   **tests:** update base64 encoding in test_transform ([97a218e](https://github.com/OneBusAway/python-sdk/commit/97a218ee3b9ee49bb19fb38e6b6d07640a3cdc8a))
-   **tests:** update sample_file.txt with newline character ([f0d7644](https://github.com/OneBusAway/python-sdk/commit/f0d76443778e46b4e3eb8f4862190c345da90c6c))
-   **trip:** update trip API endpoint to use trip_id variable ([2602a05](https://github.com/OneBusAway/python-sdk/commit/2602a0537bd4af20306c5f755ec0fb17539153d3))
-   update agency resource URL to use agency_id variable ([d600eb1](https://github.com/OneBusAway/python-sdk/commit/d600eb1146abd67cfda9a4658bf14274083c9568))
-   Update agency resource URL to use agency_id variable ([2719d60](https://github.com/OneBusAway/python-sdk/commit/2719d600837503082d3255825b721d9f577c7824))
-   Update API resource URLs to use agency_id variable ([b9c6499](https://github.com/OneBusAway/python-sdk/commit/b9c6499aaa3dc101b4a35966237aa9a161c7424a))
-   update API resource URLs to use route_id variable ([b374991](https://github.com/OneBusAway/python-sdk/commit/b37499179c139ae5af128589506bc8f4fe4ad7f5))
-   update API resource URLs to use route_id variable ([c80bdae](https://github.com/OneBusAway/python-sdk/commit/c80bdae0c9548d4deb5292911deac4ec45ce4cae))
-   Update API resource URLs to use route_id variable ([8e8f38a](https://github.com/OneBusAway/python-sdk/commit/8e8f38a467fb4515ec66c2d525de4e9355415256))
-   Update API resource URLs to use route_id variable ([b866e83](https://github.com/OneBusAway/python-sdk/commit/b866e832800bf04084bc9e2f025c8d1b326268f3))
-   Update API resource URLs to use route_id variable ([3923494](https://github.com/OneBusAway/python-sdk/commit/39234949a5688648d6c81fbea5c7c59766188cbb))
-   Update API resource URLs to use route_id variable ([0dbbc76](https://github.com/OneBusAway/python-sdk/commit/0dbbc76171b5a26cb80647f4adf9f8c6ceb003dc))
-   update API resource URLs to use stop_id variable ([26cd3ed](https://github.com/OneBusAway/python-sdk/commit/26cd3edafe208a9552eaf9a5f0bee904d8e323cd))
-   Update API resource URLs to use stop_id variable ([ea81ad9](https://github.com/OneBusAway/python-sdk/commit/ea81ad960d16f1bfc4d2b52103bd39b3ad98fbc6))
-   Update API resource URLs to use stop_id variable ([9307bb7](https://github.com/OneBusAway/python-sdk/commit/9307bb78f5229c05fc04e7e172032be12fbfb79c))
-   update API resource URLs to use trip_id variable ([0b100ed](https://github.com/OneBusAway/python-sdk/commit/0b100ed9b37db1b72fc5c0dc70e50c10c369e849))
-   Update API resource URLs to use trip_id variable ([38687b9](https://github.com/OneBusAway/python-sdk/commit/38687b97f2d1ab434576b2e78c5241e70b04d617))
-   Update API resource URLs to use trip_id variable ([c173e75](https://github.com/OneBusAway/python-sdk/commit/c173e751c71520683d8912718e121bd0d62db3ae))
-   Update API resource URLs to use trip_id variable ([7c5fddb](https://github.com/OneBusAway/python-sdk/commit/7c5fddb1668b8049d358c18152b8687a82835110))
-   update API resource URLs to use variable names ([a4f2bac](https://github.com/OneBusAway/python-sdk/commit/a4f2bacb0a5522c1ad5483ebe5b85390ac3aa728))
-   Update API resource URLs to use variable names ([fc93fe5](https://github.com/OneBusAway/python-sdk/commit/fc93fe5d36f1d0a560a41e012a7beec615340996))
-   Update API resource URLs to use variable names ([6d61f7f](https://github.com/OneBusAway/python-sdk/commit/6d61f7f605166cea6ea6655ccee9f829e33f7a8f))
-   update auth_headers method to return an empty dictionary ([ab69500](https://github.com/OneBusAway/python-sdk/commit/ab695005be6ecca41165131a5f3e7167bde6b382))
-   Update auth_headers method to return an empty dictionary ([2d7b81c](https://github.com/OneBusAway/python-sdk/commit/2d7b81ce9ca756909bfd3dc4a67d54cb19ec8aaa))
-   Update auth_headers method to return an empty dictionary ([9d1f2b7](https://github.com/OneBusAway/python-sdk/commit/9d1f2b79d1a7b7bfb2a37937d607629400523fc4))
-   Update main_sync function signature to include return type annotation ([653bb1a](https://github.com/OneBusAway/python-sdk/commit/653bb1a1d1108a1acd1a37b0fa7e6475cfede10a))
-   update the test example ([6f6fa42](https://github.com/OneBusAway/python-sdk/commit/6f6fa42d6143e53ca56b6ca5b22f0d39b3c7b963))
