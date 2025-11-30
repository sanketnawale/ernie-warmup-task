import os
import erniebot

# Set authentication
erniebot.api_type = "aistudio"
erniebot.access_token = "8e9e050008f1e71129231efbf6b7e35303da9b07"

def extract_pdf_with_ernie(pdf_path):
    """
    Use ERNIE to read and extract PDF content
    """
    print("📄 Step 1: Extracting PDF content with ERNIE...")
    
    if not os.path.exists(pdf_path):
        print(f"❌ Error: {pdf_path} not found!")
        return None
    
    try:
        # Upload file and get content
        print("   → Uploading PDF to ERNIE...")
        
        with open(pdf_path, 'rb') as f:
            # Use ERNIE's file understanding capability
            response = erniebot.ChatFile.create(
                messages=[{
                    'role': 'user',
                    'content': 'Please extract all the text content from this PDF document and format it as clean Markdown. Preserve headings, lists, and structure.'
                }],
                files=[f]
            )
        
        markdown_content = response.get_result()
        
        # Save markdown to file
        with open('extracted_content.md', 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print("   ✅ PDF extracted successfully!")
        print(f"   → Markdown saved to: extracted_content.md")
        print(f"   → Content length: {len(markdown_content)} characters")
        
        return markdown_content
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        
        # Fallback: Try direct text extraction
        print("\n   ⚠️ Trying fallback method with PyPDF2...")
        try:
            import PyPDF2
            
            text = ""
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                print(f"   → Found {len(reader.pages)} pages")
                
                for i, page in enumerate(reader.pages):
                    print(f"   → Extracting page {i+1}...")
                    text += page.extract_text() + "\n\n"
            
            # Save extracted text
            with open('extracted_content.md', 'w', encoding='utf-8') as f:
                f.write(text)
            
            print("   ✅ Text extracted with PyPDF2!")
            print(f"   → Content saved to: extracted_content.md")
            print(f"   → Content length: {len(text)} characters")
            
            return text
            
        except ImportError:
            print("   → Installing PyPDF2...")
            os.system("pip install PyPDF2")
            print("   → Please run the script again!")
            return None
        except Exception as e2:
            print(f"   ❌ Fallback also failed: {e2}")
            return None

if __name__ == "__main__":
    markdown = extract_pdf_with_ernie('input.pdf')
    
    if markdown:
        print("\n📝 Preview of extracted content:")
        print("=" * 50)
        print(markdown[:500])
        print("=" * 50)
        print("\n🎉 Step 1 Complete! Now run step2_generate_webpage.py")
