import streamlit as st
import os
import sys
import json
from typing import Dict, Any

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__)))

from agent import AWSLandingZoneAgent

# Try to import streamlit-mermaid, fallback to code display if not available
try:
    from streamlit_mermaid import st_mermaid
    MERMAID_AVAILABLE = True
except ImportError:
    MERMAID_AVAILABLE = False


def initialize_session_state():
    """Initialize Streamlit session state"""
    if 'agent' not in st.session_state:
        st.session_state.agent = AWSLandingZoneAgent()
    
    if 'current_question_index' not in st.session_state:
        st.session_state.current_question_index = 0
    
    if 'consultation_started' not in st.session_state:
        st.session_state.consultation_started = False
    
    if 'answers_complete' not in st.session_state:
        st.session_state.answers_complete = False


def render_mermaid_diagram(diagram_code: str, height: str = "400px") -> None:
    """Render Mermaid diagram using HTML/JavaScript"""
    mermaid_html = f"""
    <div id="mermaid-{hash(diagram_code)}" style="height: {height}; width: 100%;"></div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({{startOnLoad: true, theme: 'default'}});
        const element = document.getElementById('mermaid-{hash(diagram_code)}');
        const graphDefinition = `{diagram_code}`;
        mermaid.render('graph-{hash(diagram_code)}', graphDefinition).then((result) => {{
            element.innerHTML = result.svg;
        }}).catch((error) => {{
            element.innerHTML = '<p>Error rendering diagram: ' + error + '</p>';
        }});
    </script>
    """
    try:
        st.components.v1.html(mermaid_html, height=int(height.replace('px', '')) + 50)
    except AttributeError:
        # Fallback if components not available
        st.code(diagram_code, language="mermaid")


def main():
    """Main Streamlit application"""
    st.set_page_config(
        page_title="AWS Landing Zone Architect",
        page_icon="☁️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    initialize_session_state()
    
    # Sidebar
    with st.sidebar:
        st.title("☁️ AWS Landing Zone Architect")
        st.markdown("---")
        
        if st.button("🏠 Start New Assessment", use_container_width=True):
            # Reset session state
            for key in list(st.session_state.keys()):
                if key != 'agent':
                    del st.session_state[key]
            initialize_session_state()
            st.rerun()
        
        st.markdown("---")
        st.markdown("### 📋 Features")
        st.markdown("""
        - 🎯 Industry-specific AWS patterns
        - 🧠 AI-powered recommendations
        - 📊 Compliance validation
        - 🎨 Professional diagrams
        - 📑 Multi-format export
        """)
    
    # Main content
    if not st.session_state.consultation_started:
        render_welcome_page()
    elif not st.session_state.answers_complete:
        render_questionnaire()
    else:
        render_results()


def render_welcome_page():
    """Render the welcome page"""
    st.title("🏗️ AWS Landing Zone Architecture Consultant")
    st.markdown("### Expert guidance for your AWS cloud journey")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Welcome to the **AWS Landing Zone Architecture Consultant** - your intelligent guide for designing 
        enterprise-grade AWS infrastructure that meets your specific business, compliance, and security requirements.
        
        #### 🎯 What You'll Get:
        
        **📋 Comprehensive Assessment**
        - Industry-specific questionnaire
        - Compliance requirements analysis
        - Security and scalability evaluation
        
        **🧠 AI-Powered Recommendations**
        - Google Gemini AI insights
        - Industry best practices
        - Implementation guidance
        
        **🎨 Professional Diagrams**
        - Draw.io XML for desktop tools
        - Mermaid.js for web presentations
        - AWS official stencils and icons
        
        **📑 Multiple Export Formats**
        - Professional Word documents
        - JSON for automation
        - Markdown for documentation
        - Draw.io files for editing
        """)
        
        if st.button("🚀 Start AWS Assessment", type="primary", use_container_width=True):
            st.session_state.consultation_started = True
            st.rerun()
    
    with col2:
        st.info("""
        **🏭 Industries Supported:**
        - Financial Services
        - Healthcare & Life Sciences  
        - Retail & E-commerce
        - Manufacturing
        - Education
        - Government
        - And more...
        
        **🛡️ Compliance Frameworks:**
        - GDPR (EU)
        - HIPAA (Healthcare)
        - PCI DSS (Payments)
        - SOX (Financial)
        - ISO 27001
        - FedRAMP (Gov)
        """)


def render_questionnaire():
    """Render the questionnaire interface"""
    agent = st.session_state.agent
    questions = agent.get_questions()
    current_index = st.session_state.current_question_index
    
    st.title("📋 AWS Architecture Assessment")
    
    # Progress bar
    progress = (current_index + 1) / len(questions)
    st.progress(progress, text=f"Question {current_index + 1} of {len(questions)}")
    
    if current_index < len(questions):
        question = questions[current_index]
        
        st.markdown(f"### {question['question']}")
        
        if question.get('description'):
            st.markdown(f"*{question['description']}*")
        
        # Handle different question types
        if question['type'] == 'single_choice':
            options = question['options']
            selected = st.radio(
                "Select one:",
                options,
                key=f"q_{current_index}",
                index=None
            )
            
        elif question['type'] == 'multiple_choice':
            options = question['options']
            selected = st.multiselect(
                "Select all that apply:",
                options,
                key=f"q_{current_index}"
            )
            
        elif question['type'] == 'text':
            selected = st.text_input(
                "Your answer:",
                key=f"q_{current_index}"
            )
        
        elif question['type'] == 'number':
            selected = st.number_input(
                "Enter number:",
                min_value=question.get('min_value', 0),
                max_value=question.get('max_value', 1000),
                value=question.get('default_value', 1),
                key=f"q_{current_index}"
            )
        
        # Navigation buttons
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if current_index > 0:
                if st.button("← Previous", use_container_width=True):
                    st.session_state.current_question_index -= 1
                    st.rerun()
        
        with col2:
            if question.get('required', True) and not selected:
                st.button("Next →", disabled=True, use_container_width=True)
                st.warning("Please answer this question to continue.")
            else:
                if st.button("Next →", type="primary", use_container_width=True):
                    # Save answer
                    agent.save_answer(question['id'], selected)
                    
                    if current_index < len(questions) - 1:
                        st.session_state.current_question_index += 1
                    else:
                        st.session_state.answers_complete = True
                    st.rerun()
        
        with col3:
            if st.button("Skip", use_container_width=True):
                if current_index < len(questions) - 1:
                    st.session_state.current_question_index += 1
                else:
                    st.session_state.answers_complete = True
                st.rerun()


def render_results():
    """Render the results page with recommendations"""
    agent = st.session_state.agent
    
    st.title("🎯 AWS Architecture Recommendations")
    
    # Generate recommendations
    with st.spinner("Analyzing your requirements and generating recommendations..."):
        recommendation = agent.get_recommendation()
    
    # Display recommendation summary
    st.markdown("## 📊 Recommended Architecture")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"### {recommendation['pattern']['name']}")
        st.markdown(recommendation['pattern']['description'])
        
        if recommendation.get('ai_insights'):
            st.markdown("### 🧠 AI Insights")
            st.markdown(recommendation['ai_insights'])
    
    with col2:
        st.metric("Confidence Score", f"{recommendation['confidence']:.1%}")
        st.markdown("**Industry:** " + recommendation.get('industry', 'General'))
        st.markdown("**Compliance:** " + ", ".join(recommendation.get('compliance', [])))
    
    # Display architecture diagram
    st.markdown("## 🏗️ Architecture Diagram")
    
    diagram_format = st.selectbox(
        "Choose diagram format:",
        ["Mermaid (Web-friendly)", "Draw.io XML (Desktop-friendly)", "Both (Save to Files)"],
        index=0
    )
    
    if diagram_format and diagram_format.startswith("Mermaid"):
        diagram_code = agent.generate_mermaid_diagram(recommendation)
        if MERMAID_AVAILABLE:
            st_mermaid(diagram_code, height="500px")
        else:
            render_mermaid_diagram(diagram_code, "500px")
            
        # Auto-save and provide manual save option
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Save to File", use_container_width=True):
                with st.spinner("Saving Mermaid diagram..."):
                    saved_files = agent.save_diagrams(recommendation, "mermaid")
                    if saved_files:
                        st.success(f"✅ Saved to: `{saved_files['mermaid']}`")
        with col2:
            st.download_button(
                "📥 Download Mermaid",
                diagram_code,
                file_name=f"aws_architecture_{recommendation['pattern']['name'].lower().replace(' ', '_')}.md",
                mime="text/markdown"
            )
            
    elif diagram_format and diagram_format.startswith("Draw.io"):
        drawio_xml = agent.generate_drawio_diagram(recommendation)
        st.code(drawio_xml, language="xml")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("� Save to File", use_container_width=True):
                with st.spinner("Saving Draw.io diagram..."):
                    saved_files = agent.save_diagrams(recommendation, "drawio")
                    if saved_files:
                        st.success(f"✅ Saved to: `{saved_files['drawio']}`")
                        st.info("📂 Open this file in Draw.io desktop app or at app.diagrams.net")
        with col2:
            st.download_button(
                "� Download Draw.io XML",
                drawio_xml,
                file_name=f"aws_architecture_{recommendation['pattern']['name'].lower().replace(' ', '_')}.drawio",
                mime="application/xml"
            )
                    
    else:  # Both formats
        st.info("📂 This option shows both diagram formats and saves them to organized directories")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🌐 Mermaid Preview")
            diagram_code = agent.generate_mermaid_diagram(recommendation)
            if MERMAID_AVAILABLE:
                st_mermaid(diagram_code, height="400px")
            else:
                render_mermaid_diagram(diagram_code, "400px")
                
        with col2:
            st.markdown("### 🖥️ Draw.io Preview")
            drawio_xml = agent.generate_drawio_diagram(recommendation)
            st.code(drawio_xml[:500] + "...", language="xml")
            
        # Auto-save both diagrams with better UX
        st.markdown("### 💾 Save Options")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("💾 Save Both to Files", use_container_width=True):
                with st.spinner("Saving both diagrams..."):
                    saved_files = agent.save_diagrams(recommendation, "both")
                    if saved_files:
                        st.success("✅ Both diagrams saved successfully!")
                        with st.expander("📁 View saved file paths"):
                            if 'mermaid' in saved_files:
                                st.write(f"📝 **Mermaid:** `{saved_files['mermaid']}`")
                            if 'drawio' in saved_files:
                                st.write(f"🖥️ **Draw.io:** `{saved_files['drawio']}`")
                        st.info("💡 **Tip:** Open Draw.io files in Draw.io desktop app or at app.diagrams.net")
                        
        with col2:
            st.download_button(
                "� Download Mermaid",
                diagram_code,
                file_name=f"aws_architecture_{recommendation['pattern']['name'].lower().replace(' ', '_')}.md",
                mime="text/markdown",
                use_container_width=True
            )
            
        with col3:
            st.download_button(
                "📥 Download Draw.io",
                drawio_xml,
                file_name=f"aws_architecture_{recommendation['pattern']['name'].lower().replace(' ', '_')}.drawio",
                mime="application/xml",
                use_container_width=True
            )
    
    # Export options
    st.markdown("## 📑 Export Options")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📄 Export to Word", use_container_width=True):
            word_doc = agent.export_to_word(recommendation)
            st.download_button(
                "📥 Download Word Document",
                word_doc,
                file_name=f"aws_architecture_report_{agent.get_timestamp()}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    
    with col2:
        if st.button("📋 Export to JSON", use_container_width=True):
            json_data = agent.export_to_json(recommendation)
            st.download_button(
                "📥 Download JSON",
                json_data,
                file_name=f"aws_architecture_{agent.get_timestamp()}.json",
                mime="application/json"
            )
    
    with col3:
        if st.button("📝 Export to Markdown", use_container_width=True):
            markdown_data = agent.export_to_markdown(recommendation)
            st.download_button(
                "📥 Download Markdown",
                markdown_data,
                file_name=f"aws_architecture_{agent.get_timestamp()}.md",
                mime="text/markdown"
            )
    
    with col4:
        if st.button("🎨 Export Draw.io XML", use_container_width=True):
            drawio_xml = agent.generate_drawio_diagram(recommendation)
            st.download_button(
                "📥 Download Draw.io File",
                drawio_xml,
                file_name=f"aws_architecture_{agent.get_timestamp()}.drawio",
                mime="application/xml"
            )


if __name__ == "__main__":
    main()