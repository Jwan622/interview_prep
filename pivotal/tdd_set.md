## Pivotal TDD. Implement a set

The methods that I had to create were add, contains, increase size of array, isEmpty

1. The examiner started off by testing some behavior that we expect. Expected the add methods and that it should be empty
2. First test was isEmpty. He created an empty set and expected it to be empty.
```java
assertTrue(true, emptySet.isEmpty());
```
Right away you should see that this returns a boolean so you can INFER that the
minimum that you need to do to make this test pass is setup a :
```java
private Boolean isEmpty = true
```
variable at the top of your Set Class.

3. He next did a oneSet test which added something and then that test was:
```java
oneset.add("foo")
AssertFalse(oneset.isEmpty())
```

All you need to do here is let the add method switch the value of the boolean from true to false.
```java
public void add() {
  isEmpty = false;
}
```

4. Next was size.

He set up tests like this:
```java
AssertEquals(0, emptySet.size)
AssertEquals(1, oneSet.size) //assuming this has "foo" in it)
```

so your code should have a public int size variable that starts at 0. This will meausre the number of
non-null elements in the array. Also your add method should increment size every time:
```java
public int size = 0;  //at the top

```




#### Mistakes
- You didn't notice that since the test for isEmpty expected a boolean, you can get away with just returning a simple boolean in the isEmpty method. That's it. That's the simplest thing you could have done to make it pass.
- Happy and sad path. In the contains test, you should have sad path test the emptySet. Test if it contains "anything at all" and that should false. Don't just think happy path and say that it should contain something.
- During the remove method, you need to make sure you test:
1. remove something from the manySet it should no longer contain it. You said that when you remove something from the many set that the size-- that's true. But you also need to make sure that it no longer contains the object. Also you need to make sure that the set still contains the other object. For example, your many set contains "foo" and "bar". You need to make sure that if you remove "foo", it should no longer contain "foo" and that it should still contain "bar".




#### Tips for next time
-always think happy path and sad path testing
