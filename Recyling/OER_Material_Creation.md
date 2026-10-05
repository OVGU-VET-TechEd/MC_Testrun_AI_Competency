<!--
author: Educational Technology Team
email: educational.technology@atu.ie
version: 1.0.0
language: en
narrator: US English Female
comment: Interactive workshop on creating Open Educational Resources with LiaScript and GenAI for higher education
logo: <https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Tensorflow_logo.svg/1915px-Tensorflow_logo.svg.png>

@style
.tool-card {
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
color: white;
padding: 2rem;
margin: 1rem;
border-radius: 15px;
box-shadow: 0 8px 32px rgba(0,0,0,0.3);
transition: transform 0.3s ease;
}

.tool-card:hover {
transform: translateY(-5px);
}

.workflow-step {
background: #f8f9fa;
border: 2px solid #007bff;
border-radius: 10px;
padding: 1.5rem;
margin: 1rem 0;
}

.prompt-template {
background: linear-gradient(45deg, #ff6b6b, #ffa726);
color: white;
padding: 1rem;
border-radius: 10px;
margin: 1rem 0;
}

.resource-link {
background: #28a745;
color: white;
padding: 0.5rem 1rem;
border-radius: 5px;
text-decoration: none;
display: inline-block;
margin: 0.25rem;
transition: all 0.3s ease;
}

.resource-link:hover {
background: #218838;
transform: scale(1.05);
}

.live-demo {
background: #e3f2fd;
border-left: 4px solid #2196f3;
padding: 1rem;
margin: 1rem 0;
}
@end

@toolCard: <div class="tool-card">**🔧 @0**<br />@1</div>

@workflowStep: <div class="workflow-step">**📋 Step @0:** @1<br />@2</div>

@promptTemplate: <div class="prompt-template">**🤖 Prompt Template:** @0<br /><br />`<br>@1<br>`</div>

@resourceLink: <a href="@1" class="resource-link" target="\_blank">@0</a>

@liveDemo: <div class="live-demo">**🎯 Live Demo:** @0</div>

\-->

# Open Educational Resources – Learning Material Development (incl. use of GenAI)

<svg xmlns='http://www.w3.org/2000/svg' width='1100' height='400' viewBox='0 0 800 450'>
<!-- Background -->
<rect width='800' height='450' fill='#2196f3' />
<!-- White rounded rectangle container -->
<rect x='50' y='50' width='700' height='350' rx='20' fill='white' />
<!-- Main Title -->
<text x='400' y='90' font-family='Segoe UI, Arial, sans-serif' font-size='24' font-weight='bold' text-anchor='middle' fill='#2196f3'>
Open Educational Resources
</text>
<text x='400' y='120' font-family='Segoe UI, Arial, sans-serif' font-size='24' font-weight='bold' text-anchor='middle' fill='#2196f3'>
Learning Material Development
</text>
<text x='400' y='150' font-family='Segoe UI, Arial, sans-serif' font-size='20' font-weight='bold' text-anchor='middle' fill='#2196f3'>
with LiaScript and GenAI
</text>
<!-- Subtitle -->
<text x='400' y='190' font-family='Segoe UI, Arial, sans-serif' font-size='16' font-weight='bold' text-anchor='middle' fill='#666'>
Workshop for Teacher Trainers & Higher Educators
</text>
<!-- Institution -->
<text x='400' y='220' font-family='Segoe UI, Arial, sans-serif' font-size='14' font-weight='bold' text-anchor='middle' fill='#999'>
Atlantic Technical University
</text>
<text x='400' y='240' font-family='Segoe UI, Arial, sans-serif' font-size='14' text-anchor='middle' fill='#999'>
Galway Campus
</text>
<!-- Example -->
<text x='400' y='280' font-family='Segoe UI, Arial, sans-serif' font-size='16' font-weight='bold' text-anchor='middle' fill='#2196f3'>
Example Module: Digital Pedagogy Fundamentals
</text>
<!-- Tools -->
<text x='400' y='310' font-family='Segoe UI, Arial, sans-serif' font-size='12' text-anchor='middle' fill='#666'>
Tools: ChatGPT • Perplexity • Claude • GitHub • Gamma.app
</text>
<!-- Date -->
<text x='400' y='340' font-family='Segoe UI, Arial, sans-serif' font-size='12' text-anchor='middle' fill='#666'>
Professional Development Session 2025
</text>
</svg>

---

## 🎯 Workshop Goals

**Learning Objectives:**

- Understand how LiaScript and GenAI can enhance OER development in higher education
- Master the 6-step AI-enhanced workflow for creating interactive learning materials
- Experience hands-on creation using "Digital Pedagogy Fundamentals" as our example
- Implement quality assurance through multiple AI tools
- Deploy materials through GitHub and create multiple output formats for diverse learning contexts

**Target Challenges We're Solving:**

- Faculty struggling with time-intensive content creation for diverse student needs
- Need for accessible, inclusive learning materials that meet Universal Design for Learning principles
- Bridging the gap between traditional teaching methods and digital pedagogical approaches
- Scalable content development that accommodates varying technical expertise levels

---

## 🏛️ The Higher Education Teaching Challenge

### Current Situation in Irish Higher Education

**Common Faculty Challenges:**

- Increasing class sizes with diverse learning needs and backgrounds
- Limited time for developing interactive, accessible teaching materials
- Pressure to integrate digital technologies meaningfully into curriculum
- Need for multilingual and culturally inclusive content
- Balancing research responsibilities with innovative teaching practices

**Institutional Pressures:**

- Quality assurance requirements for program delivery
- Digital transformation mandates post-COVID
- Student expectations for engaging, flexible learning experiences
- Need for evidence-based pedagogical approaches
- Sustainability and cost-effectiveness in resource development

### 💡 LiaScript + GenAI Solution

**Why This Approach for Higher Education?**

- **Text-Based Creation** - Academics can leverage existing writing skills
- **Interactive Elements** - Enhance student engagement without complex coding
- **Multi-Format Output** - Supports diverse learning preferences and accessibility needs
- **Version Control** - Academic rigor in content development and collaboration
- **Open Source Ethos** - Aligns with educational values and budget constraints
- **Pedagogical Integration** - Embed evidence-based teaching strategies directly into content

---

## 🔧 Our 6-Step AI-Enhanced Workflow

### Overview of the Process

@workflowStep(1, ChatGPT for Pedagogical Structure, Generate learning objectives and evidence-based instructional design)
@workflowStep(2, Perplexity for Academic Research, Validate current educational research and best practices)  
@workflowStep(3, Claude for LiaScript, Create interactive markdown content with pedagogical scaffolding)
@workflowStep(4, GitHub Repository, Academic collaboration and version control)
@workflowStep(5, Export Formats, Generate accessible PDFs and LMS-compatible packages)
@workflowStep(6, Gamma.app Presentations, Create conference and workshop materials)

**Example Module:** Digital Pedagogy Fundamentals

**Time Investment:** ~4-6 hours total for a complete learning module

---

## 📝 Step 1: ChatGPT for Pedagogical Structure

### Goal: Generate Evidence-Based Learning Design

@liveDemo(Let's create our Digital Pedagogy module structure together!)

@promptTemplate(Academic Module Structure, You are an expert in higher education pedagogy and instructional design, specializing in teacher training programs.

Create a comprehensive module outline for "Digital Pedagogy Fundamentals" targeted at teacher trainers and higher education faculty who need to integrate digital technologies meaningfully into their teaching practice.

The module should:

- Be grounded in established pedagogical frameworks (e.g., TPACK, UDL, Bloom's Taxonomy)
- Include diverse assessment strategies suitable for adult learners
- Address different learning styles and accessibility requirements
- Be suitable for both face-to-face and online delivery
- Take approximately 6-8 hours across multiple sessions

Structure your response as:

1. Module overview with theoretical framework
2. 5-7 learning outcomes aligned with professional teaching standards
3. Session-by-session breakdown with active learning strategies
4. Formative and summative assessment approaches
5. Resources for further professional development
6. Integration strategies for participants' own teaching contexts

Focus on practical application while maintaining academic rigor expected in higher education.)

**Interactive Exercise:** Let's run this prompt together and see what ChatGPT generates!

```
{{1}}
```

<section>

### Expected Output Structure

**Sample Module Sessions:**

1. Theoretical Foundations of Digital Pedagogy
2. Technology Integration Models (TPACK Framework)
3. Universal Design for Learning in Digital Environments
4. Assessment in Digital Learning Contexts
5. Creating Inclusive Digital Content
6. Student Engagement Strategies Online
7. Reflective Practice and Continuous Improvement

</section>

---

## 🔍 Step 2: Perplexity for Academic Research

### Goal: Validate Current Educational Research

@liveDemo(Ensuring our content reflects latest pedagogical research)

@promptTemplate(Academic Validation, I'm developing a professional development module on "Digital Pedagogy Fundamentals" for higher education faculty. Please validate and enhance the following content with current educational research:

[PASTE CHATGPT OUTPUT HERE]

Specifically, please:

1. Verify alignment with current higher education teaching standards (e.g., PSF, HEA Fellowship descriptors)
2. Identify recent research (2020-2025) supporting the pedagogical approaches mentioned
3. Suggest evidence-based digital tools and platforms currently used in higher education
4. Highlight any accessibility and inclusion considerations that should be emphasized
5. Provide examples from Irish or European higher education contexts where possible
6. Update any theoretical frameworks or models with recent developments

Please cite academic sources where possible and highlight any corrections or additions based on current research.)

**Key Areas to Research:**

- Latest pedagogical research on digital learning effectiveness
- Current accessibility standards (WCAG 2.1, EN 301 549)
- European higher education digital competence frameworks
- Post-pandemic shifts in educational technology adoption
- Evidence on student engagement in hybrid learning environments

  {{1}}
  <section>

### Research Quality Checklist

**Academic Rigor:**

- [ ] Sources from peer-reviewed educational journals
- [ ] Alignment with established pedagogical frameworks
- [ ] Current accessibility and inclusion standards
- [ ] Evidence-based teaching strategies included

**Contextual Relevance:**

- [ ] Irish higher education context considered
- [ ] European qualification frameworks referenced
- [ ] Professional development standards addressed
- [ ] Practical applicability verified

</section>

---

## 🤖 Step 3: Claude for LiaScript Creation

### Goal: Transform Content into Interactive Learning Experience

@liveDemo(Converting our module into engaging LiaScript format)

@promptTemplate(LiaScript Educational Design, You are an expert in creating educational content using LiaScript markdown format for higher education contexts.

Convert the following validated module content into a comprehensive LiaScript document:

[PASTE VALIDATED CONTENT FROM PERPLEXITY HERE]

Requirements:

1. Include proper LiaScript metadata targeting higher education faculty
2. Create pedagogically sound interactive elements:
   - Reflection prompts for adult learners
   - Knowledge check quizzes based on learning outcomes
   - Case study analysis activities
   - Collaborative discussion prompts
3. Add text-to-speech for accessibility
4. Include proper academic section navigation
5. Use LiaScript's formatting for:
   - Code blocks for digital tools demonstration
   - Mathematical formulas (for learning analytics)
   - Interactive charts for pedagogical models
6. Add ASCII art diagrams for theoretical frameworks
7. Include comprehensive assessment section with rubrics

Educational Context: Ensure all content is appropriate for adult learners (teacher trainers and higher education faculty) and includes opportunities for reflection on their own teaching practice.

Target Audience: Experienced educators seeking to enhance their digital pedagogy skills while maintaining academic standards.)

**Interactive Exercise:** Let's convert a section together!

```
{{1}}
```

<section>

### LiaScript Educational Features to Include

**Interactive Pedagogical Elements:**

- `?[Reflection Questions]` for critical thinking
- `[[Case Study Analysis]]` for practical application
- Collaborative discussion spaces
- Self-assessment rubrics

**Higher Education Specific Examples:**

- Learning management system integration
- Academic assessment design
- Research-informed teaching practices
- Professional development planning

</section>

```
{{2}}
```

<section>

### Sample LiaScript Structure

```markdown
<!--
author: Educational Technology Team, ATU Galway
email: educational.technology@atu.ie
version: 1.0.0
language: en
narrator: US English Female
-->

# Digital Pedagogy Fundamentals

## Session 1: Theoretical Foundations

--{{0}}--
Welcome to Digital Pedagogy Fundamentals. This module is designed 
for higher education faculty and teacher trainers who want to 
integrate digital technologies meaningfully into their teaching practice.

    {{1}}
Let's begin by reflecting on your current teaching approach:

### Self-Reflection Activity

Consider a recent teaching session you delivered. How did you:
- Engage students with the content?
- Assess their understanding?
- Accommodate different learning styles?

### TPACK Framework Introduction

The Technological Pedagogical Content Knowledge (TPACK) framework 
provides a foundation for meaningful technology integration.

What aspect of TPACK do you find most challenging in your teaching context?

    [( )] Technology Knowledge
    [( )] Pedagogical Knowledge  
    [( )] Content Knowledge
    [(X)] Integration of all three
    [( )] I'm not familiar with TPACK
```

</section>

---

## 📂 Step 4: GitHub Repository for Academic Collaboration

### Goal: Enable Scholarly Collaboration and Version Control

@liveDemo(Setting up our academic repository)

**Repository Structure for Higher Education:**

```
digital-pedagogy-fundamentals/
├── README.md
├── modules/
│   ├── session-01-foundations.md
│   ├── session-02-tpack.md
│   ├── session-03-udl.md
│   └── session-04-assessment.md
├── resources/
│   ├── readings/
│   ├── templates/
│   └── multimedia/
├── assessments/
│   ├── rubrics/
│   └── portfolios/
├── exports/
│   ├── pdf/
│   ├── scorm/
│   └── presentations/
└── collaboration/
    ├── peer-review-guidelines.md
    └── contribution-templates.md
```

@promptTemplate(Academic Repository Setup, Create a comprehensive README.md file for our "Digital Pedagogy Fundamentals" module repository targeted at higher education faculty.

Include:

 1. Module description aligned with professional teaching standards
 2. Learning outcomes and assessment criteria
 3. Prerequisites and target participant profile
 4. How to access and navigate the materials (LiaScript integration)
 5. Technical requirements and accessibility considerations
 6. Module structure with estimated completion times
 7. How colleagues can contribute and provide academic peer review
 8. Export options for different institutional LMS platforms
 9. Licensing information (Creative Commons)
10. Contact information for module coordinators at ATU Galway

Maintain academic tone while being accessible to faculty with varying technical expertise.)

```
{{1}}
```

<section>

### Academic Collaboration Benefits

**Scholarly Version Control:**

- Track pedagogical improvements and iterations
- Collaborate across institutions and disciplines
- Maintain academic integrity in content development

**Open Educational Resources:**

- CC licensing for broad educational use
- Peer review processes for quality assurance
- Community-driven improvement and localization

**Institutional Integration:**

- Connect with ATU's academic quality systems
- Align with professional development frameworks
- Support evidence-based teaching enhancement

</section>

---

## 📄 Step 5: Multi-Format Outputs for Educational Contexts

### Goal: Support Diverse Learning and Institutional Needs

@liveDemo(Generating accessible formats for our module)

**PDF Export for Academic Use:**

- **Accessible PDF:** WCAG 2.1 compliant for inclusive access
- **Print-friendly:** Remove interactive elements for offline study
- **Portfolio versions:** Include reflection spaces for CPD evidence

**LMS Integration Packages:**

- **SCORM 2004:** Full interactivity with progress tracking
- **Moodle backup:** Direct import to institutional systems
- **Canvas Commons:** Shareable course materials
- **Offline packages:** Download for limited connectivity contexts

@workflowStep(5a, Accessible PDF Creation, Generate WCAG-compliant PDFs with proper heading structure and alt text)
@workflowStep(5b, LMS Package Development, Create SCORM packages compatible with major learning management systems)
@workflowStep(5c, Quality Assurance, Test accessibility compliance and cross-platform functionality)

```
{{1}}
```

<section>

### Technical Implementation for Higher Education

**Automated Academic Publishing:**

```yaml
# GitHub Action for educational exports
name: Academic Content Publishing
on:
  push:
    paths: ['modules/**/*.md']
    
jobs:
  academic-export:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Generate Accessible PDF
        run: |
          pandoc modules/*.md -o exports/pedagogy-module.pdf \
          --pdf-engine=xelatex --include-in-header=accessibility.tex
      - name: Create SCORM Package
        run: |
          liascript-exporter --scorm modules/ exports/scorm/
      - name: Validate Accessibility
        run: |
          pa11y-ci exports/
```

</section>

---

## 🎨 Step 6: Professional Presentations with Gamma.app

### Goal: Create Conference-Ready Materials

@liveDemo(Building presentation materials for academic conferences)

@promptTemplate(Academic Conference Presentation, Create an engaging conference presentation from our "Digital Pedagogy Fundamentals" module for presentation at educational technology conferences.

Structure the presentation for higher education faculty and educational developers:

1. Title slide with institutional affiliation and author details
2. Context: Challenges in higher education digital transformation (2-3 slides)
3. Theoretical framework: OER and AI-enhanced content creation (2 slides)
4. Methodology: Our 6-step workflow with academic rationale (3-4 slides)
5. Case study: Digital Pedagogy Fundamentals module development (2-3 slides)
6. Results: Learning outcomes and faculty feedback (2 slides)
7. Implications for practice and institutional adoption (2 slides)
8. Future research directions and sustainability (1 slide)
9. References and contact information (1 slide)

Style requirements:

- Academic conference standard formatting
- Include relevant educational theory citations
- Use professional typography and Atlantic Technical University branding where appropriate
- Balance text with meaningful visuals and data
- Include slide notes for presentation delivery

Tone: Scholarly but accessible, emphasizing evidence-based practice and practical implementation.)

**Gamma.app Features for Academic Use:**

- **Research-informed templates:** Educational conference standards
- **Citation integration:** Automatic reference formatting
- **Data visualization:** Present learning analytics and outcomes
- **Institutional branding:** ATU Galway visual identity compliance

  {{1}}
  <section>

### Presentation Strategy for Academic Audiences

**For Educational Developers:**

- Emphasize pedagogical theory and evidence base
- Highlight scalability and institutional impact
- Show integration with existing faculty development programs
- Demonstrate measurable learning outcomes

**For Faculty Researchers:**

- Focus on methodology and replicability
- Present data on efficiency gains and learning effectiveness
- Discuss implications for open educational practices
- Highlight opportunities for educational research collaboration

</section>

---

## 🎯 Live Workshop Activity

### Creating Our Pedagogy Module Together

Let's work through each step using our "Digital Pedagogy Fundamentals" example:

```
{{0-1}}
```

**Step 1 Activity:** ChatGPT Pedagogical Structure

> Open ChatGPT and use our educational design prompt to generate the module outline

```
{{1-2}}
```

**Step 2 Activity:** Perplexity Academic Research

> Take the ChatGPT output and validate it using current educational research

```
{{2-3}}
```

**Step 3 Activity:** Claude LiaScript Development

> Convert one session into interactive LiaScript format

```
{{3-4}}
```

**Step 4 Activity:** GitHub Academic Repository

> Set up a collaborative repository for peer review and sharing

```
{{4-5}}
```

**Step 5 Activity:** Multi-Format Export Testing

> Generate accessible PDFs and LMS packages

```
{{5-6}}
```

**Step 6 Activity:** Conference Presentation Creation

> Create a presentation for sharing at educational conferences

### Reflection Questions for Educators

After completing the activities, consider:

- How does this workflow align with your current content development practices?
- What barriers might exist in your institutional context?
- How could you adapt this approach for your specific discipline or student population?
- What additional pedagogical considerations are important for your context?

---

## 📊 Implementation Strategy for Higher Education

### Phase 1: Faculty Pilot Program (Semester 1)

- Start with 3-5 volunteer faculty from different disciplines
- Focus on high-impact, reusable content (e.g., research methods, critical thinking)
- Integrate with existing professional development programs

### Phase 2: Departmental Adoption (Semester 2-3)

- Expand to department-level implementation
- Train educational developers and learning technologists
- Establish peer review and quality assurance processes

### Phase 3: Institution-wide Integration (Year 2)

- Roll out to all schools and departments
- Integrate with promotion and tenure processes for teaching excellence
- Establish communities of practice and ongoing support

@workflowStep(Success Metrics, Measure faculty engagement, student learning outcomes, and content reuse rates, Track professional development participation and teaching innovation evidence)

---

## 🔧 Templates and Resources for Educators

### Academic Planning Templates

**Module Planning Template:**

```markdown
# Module: [Subject Area]
**Target Audience:** [Faculty/Student Level]
**Learning Framework:** [TPACK/UDL/Constructivism etc.]
**Duration:** [Contact Hours + Self-Study]
**Learning Outcomes:** 
1. [Cognitive Level - Knowledge/Comprehension/Application]
2. [Skills Development]
3. [Professional Practice Integration]

**Assessment Strategy:** [Formative + Summative approaches]
**Accessibility Considerations:** [UDL principles applied]
```

**Academic Resource Library:**
@resourceLink(Educational Research Prompts, #research-prompts)
@resourceLink(Pedagogical Framework Templates, #pedagogy-templates)  
@resourceLink(LiaScript Academic Examples, #liascript-examples)
@resourceLink(Higher Education GitHub Resources, #github-academic)

### Educational Technology Resources

@resourceLink(LiaScript Educational Documentation, https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md)
@resourceLink(Universal Design for Learning Guidelines, https://udlguidelines.cast.org/)
@resourceLink(European Standards for Digital Competence, https://ec.europa.eu/jrc/en/digcomp)
@resourceLink(Creative Commons Licensing for Education, https://creativecommons.org/share-your-work/)

---

## 💡 Advanced Features for Higher Education

### Enhanced Pedagogical Interactivity

**Advanced LiaScript Educational Features:**

- **Adaptive Learning Paths:** Content branching based on prior knowledge assessment
- **Collaborative Annotation:** Peer learning and discussion integration
- **Learning Analytics:** Progress tracking and intervention points
- **Multi-modal Content:** Support for diverse learning preferences

**GenAI Integration for Personalization:**

- **Individualized Feedback:** AI-generated formative assessment responses
- **Content Adaptation:** Adjust complexity based on learner progress
- **Language Support:** Multi-language content generation for international students

### Institutional Scaling Considerations

**Academic Quality Assurance:**

- Establish peer review processes for AI-generated content
- Align with institutional teaching and learning strategies
- Create guidelines for ethical AI use in education
- Plan for accessibility compliance and inclusive design

**Professional Development Integration:**

- Connect to continuing professional development frameworks
- Support evidence portfolios for teaching excellence recognition
- Facilitate communities of practice around innovative pedagogy
- Provide ongoing technical and pedagogical support

---

## ❓ Q&A and Discussion for Higher Educators

### Common Academic Questions

**"How do we ensure academic rigor while using AI-assisted content creation?"**

> The 6-step workflow includes multiple validation steps and peer review processes that maintain scholarly standards while improving efficiency.

**"What about academic integrity and originality in AI-generated educational content?"**

> AI is used as a pedagogical design tool rather than content generator - faculty expertise guides the process, with AI supporting structure and interactivity.

**"How does this align with our quality assurance and accreditation requirements?"**

> The approach supports evidence-based teaching practices and can strengthen quality documentation through version control and peer collaboration.

### Discussion Topics for ATU Context

- How can this approach support ATU's strategic goals for innovative teaching?
- What specific disciplines or programs would benefit most from this methodology?
- How can we integrate this with existing Moodle and educational technology infrastructure?
- What professional development support would faculty need for successful adoption?

---

## 🚀 Action Items and Next Steps for ATU Galway

### Immediate Actions (This Month)

- [ ] Identify champion faculty from different schools for pilot participation
- [ ] Set up institutional GitHub organization for educational content collaboration
- [ ] Connect with Educational Development Unit for integration planning
- [ ] Assess current technical infrastructure and support needs

### Short-term Goals (Next Semester)

- [ ] Complete pilot module development with 3-5 faculty participants
- [ ] Integrate with existing professional development program offerings
- [ ] Gather student and faculty feedback for iterative improvement
- [ ] Document best practices and institutional guidelines

### Long-term Vision (Academic Year)

- [ ] Scale to department-level adoption across multiple schools
- [ ] Establish ATU as a leader in innovative OER development
- [ ] Create inter-institutional collaborations and resource sharing
- [ ] Measure impact on teaching excellence and student outcomes

**Contact Information:**

- Educational Technology Team: educational.technology@atu.ie
- Learning & Teaching Unit: teaching@atu.ie
- Repository Access: github.com/atu-galway/educational-resources

---

**Thank you for participating in this Professional Development Workshop!**

> Ready to transform higher education through innovative, AI-enhanced Open Educational Resources?

**Final Reflection for Educators:**
What will be your first module topic, and how will you adapt this workflow to meet your students' specific learning needs and your disciplinary context?

<!-- License info -->
<div style="position: fixed; bottom: 10px; right: 10px; font-size: 12px; opacity: 0.7;">
<img src="https://licensebuttons.net/l/by-sa/4.0/80x15.png" alt="CC BY-SA" style="height: 20px; vertical-align: middle;">
<a href="https://creativecommons.org/licenses/by-sa/4.0/" style="margin-left: 5px; text-decoration: none;">CC BY-SA 4.0</a>
</div>