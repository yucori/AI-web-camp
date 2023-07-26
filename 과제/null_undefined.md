# null과 undefined

---

## null

- null은 아무것도 없는 "무"의 상태가 아니다. 아무 것도 정의되지 않은 것이 아니라, 비어있으라 정의한 것이다. 해당 변수가 아무것도 가리키고 있지 않다는 것을 의미한다. 그래서 typeof null은 객체가 출력된다.

## undefined

- undefined는 변수가 선언된 뒤에 아무것도 할당되지 않았을 경우에 할당된다. 함수가 값을 return 하지 않을 때에는 undefined가 출력된다. 따라서 typeof null은 undefined가 출력된다.

## null과 undefined 출력 예제

```
typeof null // 'object'
typeof undefined // 'undefined'
null === undefined // false
null == undefined // true
null === null // true
null == null // true
!null // true
isNaN(1 + null) // false
isNaN(1 + undefined) // true
```
