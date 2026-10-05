# LiaScript cheatsheet (the subset used in MC01)

## Header (identical in every module; the combine script keeps only M0's, so M0 must contain ALL style classes)

```markdown
<!--
author:   Hannes Tegelbeckers
email:    hannes.tegelbeckers@ovgu.de
version:  0.1.0
language: en
narrator: UK English Female
mode:     Textbook
comment:  MCxx · Module n: Title (x h)

@style
.headline { border: 2px dashed #c62828; padding: .8em 1em; font-family: Georgia, serif; font-size: 1.15em; border-radius: 6px; }
.precise  { border-left: 6px solid #2e7d32; background: rgba(46,125,50,.08); padding: .6em 1em; border-radius: 6px; }
.journal  { border-left: 6px solid #6a1b9a; background: rgba(106,27,154,.08); padding: .6em 1em; border-radius: 6px; }
.deepdive { border-left: 6px solid #1565c0; background: rgba(21,101,192,.08); padding: .6em 1em; border-radius: 6px; }
.poe      { border-left: 6px solid #ef6c00; background: rgba(239,108,0,.08); padding: .6em 1em; border-radius: 6px; }
@end
-->
```

## Styled boxes

Put a class comment on the line before a blockquote:

```markdown
<!-- class="precise" -->
> 🟩 **Precise Language Box**
> ...
```

Box vocabulary: 📰 headline · 🟩 precise · 🟪 journal · 🟦 deepdive · 🔮 poe.

## Quizzes

| Type | Syntax |
|---|---|
| Single choice | `[(X)] correct` / `[( )] wrong` |
| Multiple choice | `[[X]] correct` / `[[ ]] wrong` |
| Text (exact match, so keep answers to 1 word) | `[[answer]]` |
| Inline selection | `The model [[ thinks | (computes) | feels ]] the result.` |
| Hint | `[[?]] hint text` under the quiz |
| Solution/explanation shown after solving | block between two lines of `****************************************` |

## Surveys (not graded; answers stored in the browser)

| Type | Syntax |
|---|---|
| Free text, n lines | `[[___]]`, `[[___ ___ ___]]` |
| Single-choice survey / scale | `[(1)] option` `[(2)] option` |
| Multiple-choice survey | `[[a]] option` `[[b]] option` |

## Runnable JavaScript

````markdown
```js
var x = 1;            // learners can edit
console.log(x);
```
<script>@input</script>
````

Keep it ES5 (`var`, `function`), no DOM access, output via `console.log`.
Test locally: `/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc`
with `var console={log:print};` prepended.

## Other

- Narration: `--{{0}}--` on its own line, then a paragraph that is read aloud (used sparingly).
- ASCII diagrams: a ```` ```ascii ```` code block.
- Collapsible model answers: `<details><summary>💡 …</summary> … </details>` (blank lines inside!).
- Page = every `#`/`##` heading. Keep pages short; put `> ⏱ nn min` directly under each heading.
